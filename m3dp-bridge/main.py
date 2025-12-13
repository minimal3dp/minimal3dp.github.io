from fastapi import FastAPI, HTTPException, Request, Depends, BackgroundTasks, Form, status
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import create_engine, select, update, delete
import secrets
from sqlalchemy.orm import sessionmaker, Session
from contextlib import asynccontextmanager
import os
from .models import Base, AffiliateLink, Printer

# Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/m3dp")

# Database Setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Lifecycle
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create tables if not exist (for MVP)
    # In production, use Alembic migrations
    try:
        Base.metadata.create_all(bind=engine)
        print("Database initialized.")
    except Exception as e:
        print(f"Database init skipped (connection might be missing): {e}")
    yield
    # Shutdown

app = FastAPI(
    title="M3DP-BRIDGE",
    description="Minimal 3DP Hardware Bridge & Smart Link System",
    lifespan=lifespan
)

# --- Security ---
security = HTTPBasic()

def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = os.getenv("ADMIN_USERNAME", "admin")
    correct_password = os.getenv("ADMIN_PASSWORD", "change_me_in_prod")
    
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = correct_username.encode("utf8")
    is_correct_username = secrets.compare_digest(current_username_bytes, correct_username_bytes)
    
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = correct_password.encode("utf8")
    is_correct_password = secrets.compare_digest(current_password_bytes, correct_password_bytes)
    
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# --- Routes ---

@app.get("/")
def read_root():
    return {"status": "M3DP-BRIDGE Online", "mission": "Hardware Bridge"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

async def log_click(link_slug: str, db: Session):
    """Background task to increment click count."""
    try:
        stmt = (
            update(AffiliateLink)
            .where(AffiliateLink.slug == link_slug)
            .values(clicks=AffiliateLink.clicks + 1)
        )
        db.execute(stmt)
        db.commit()
    except Exception as e:
        print(f"Failed to log click for {link_slug}: {e}")

@app.get("/go/{slug}")
async def smart_redirect(slug: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Smart Link Redirector.
    Looks up slug, logs click (async), redirects to target.
    """
    stmt = select(AffiliateLink).where(AffiliateLink.slug == slug)
    result = db.execute(stmt)
    link = result.scalar_one_or_none()

    if not link:
        # Fallback or 404
        # For now, just 404. Later could redirect to search.
        raise HTTPException(status_code=404, detail="Link not found")

    # Log click in background to not block redirect
    # We need a new session for background task or careful handling, 
    # but for simple increment, we can do it here or pass to bg task.
    # Safe way: do it here synchronously for MVP or pass ID to bg task.
    link.clicks += 1
    db.commit()

    return RedirectResponse(url=link.target_url)

# --- Admin / Dashboard ---

@app.post("/links", dependencies=[Depends(verify_admin)])
def create_link(slug: str = Form(...), target_url: str = Form(...), db: Session = Depends(get_db)):
    # Simple create
    try:
        new_link = AffiliateLink(slug=slug, target_url=target_url)
        db.add(new_link)
        db.commit()
    except Exception as e:
        # Duplicate slug?
        print(f"Error creating link: {e}")
        pass
    return RedirectResponse(url="/dashboard", status_code=303)

@app.post("/links/{id}/delete", dependencies=[Depends(verify_admin)])
def delete_link(id: int, db: Session = Depends(get_db)):
    stmt = delete(AffiliateLink).where(AffiliateLink.id == id)
    db.execute(stmt)
    db.commit()
    return RedirectResponse(url="/dashboard", status_code=303)

@app.get("/dashboard", response_class=HTMLResponse, dependencies=[Depends(verify_admin)])
def dashboard(db: Session = Depends(get_db)):
    # Minimal HTMX dashboard
    stmt = select(AffiliateLink).order_by(AffiliateLink.clicks.desc())
    links = db.execute(stmt).scalars().all()
    
    html = """
    <html>
    <head><title>M3DP-BRIDGE Dashboard</title></head>
    <body style="font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem;">
        <h1>M3DP-BRIDGE Command Center</h1>
        
        <div style="background: #f0f0f0; padding: 1rem; margin-bottom: 2rem; border-radius: 4px;">
            <h3>Create New Smart Link</h3>
            <form action="/links" method="post" style="display: flex; gap: 10px;">
                <input type="text" name="slug" placeholder="Slug (e.g. k2-gears)" required style="padding: 5px;">
                <input type="url" name="target_url" placeholder="Target URL (Amazon/Ali)" required style="padding: 5px; flex-grow: 1;">
                <button type="submit" style="background: #007bff; color: white; border: none; padding: 5px 15px; cursor: pointer;">Create</button>
            </form>
        </div>

        <h2>Active Links</h2>
        <table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
            <thead><tr><th>Slug</th><th>Target</th><th>Clicks</th><th>Action</th></tr></thead>
            <tbody>
    """
    for link in links:
        html += f"""
        <tr>
            <td><a href="/go/{link.slug}" target="_blank">{link.slug}</a></td>
            <td>{link.target_url[:50]}...</td>
            <td>{link.clicks}</td>
            <td>
                <form action="/links/{link.id}/delete" method="post" style="margin: 0;">
                    <button type="submit" style="background: #dc3545; color: white; border: none; padding: 2px 8px; cursor: pointer;">Delete</button>
                </form>
            </td>
        </tr>
        """
    
    html += """
            </tbody>
        </table>
    </body>
    </html>
    """
    return html
