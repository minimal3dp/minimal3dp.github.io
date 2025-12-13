FROM python:3.11-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy project definition
COPY pyproject.toml .

# Install dependencies
# --system installs into the system python environment, avoiding the need for a venv in the container
RUN uv pip install --system -r pyproject.toml

# Copy application code
COPY . /app/m3dp-bridge

CMD ["uvicorn", "m3dp-bridge.main:app", "--host", "0.0.0.0", "--port", "8000"]
