from sqlalchemy import String, Integer, Boolean, JSON, ForeignKey, UniqueConstraint, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional

class Base(DeclarativeBase):
    pass

class Printer(Base):
    __tablename__ = "printers"

    id: Mapped[int] = mapped_column(primary_key=True)
    make: Mapped[str] = mapped_column(String, index=True)
    model: Mapped[str] = mapped_column(String, index=True)
    kinematics: Mapped[str] = mapped_column(String)  # Enum: CoreXY, Cartesian, Delta
    build_volume: Mapped[dict] = mapped_column(JSONB)  # {"x": 256, "y": 256, "z": 256}
    firmware: Mapped[str] = mapped_column(String)  # Enum: Klipper, Marlin

    profiles: Mapped[List["SlicerProfile"]] = relationship(back_populates="printer")

    def __repr__(self):
        return f"<Printer {self.make} {self.model}>"

class Filament(Base):
    __tablename__ = "filaments"

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String, index=True)
    material: Mapped[str] = mapped_column(String)  # Enum: PLA, PETG, ABS, ASA
    density: Mapped[float] = mapped_column(Float, default=1.24)
    temp_range: Mapped[str] = mapped_column(String)  # "200-220"

    profiles: Mapped[List["SlicerProfile"]] = relationship(back_populates="filament")

    def __repr__(self):
        return f"<Filament {self.brand} {self.material}>"

class SlicerProfile(Base):
    __tablename__ = "slicer_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    printer_id: Mapped[int] = mapped_column(ForeignKey("printers.id"))
    filament_id: Mapped[int] = mapped_column(ForeignKey("filaments.id"))
    profile_name: Mapped[str] = mapped_column(String)
    config_data: Mapped[dict] = mapped_column(JSONB) # Full config key-values
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    
    printer: Mapped["Printer"] = relationship(back_populates="profiles")
    filament: Mapped["Filament"] = relationship(back_populates="profiles")

    __table_args__ = (
        UniqueConstraint("printer_id", "filament_id", "profile_name", name="uix_profile"),
    )

    def __repr__(self):
        return f"<SlicerProfile {self.profile_name}>"

class AffiliateLink(Base):
    __tablename__ = "affiliate_links"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String, unique=True, index=True)
    target_url: Mapped[str] = mapped_column(String)
    clicks: Mapped[int] = mapped_column(Integer, default=0)
    revenue_category: Mapped[Optional[str]] = mapped_column(String)

    def __repr__(self):
        return f"<AffiliateLink /go/{self.slug} -> {self.target_url}>"
