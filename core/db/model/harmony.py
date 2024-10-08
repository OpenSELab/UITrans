from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from core.db.model.base import Base


class HarmonyComponentExample(Base):
    __tablename__ = "harmony_component_example"

    api_version: Mapped[str] = mapped_column(default="12")
    component_name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    code: Mapped[str] = mapped_column(Text, nullable=False)
