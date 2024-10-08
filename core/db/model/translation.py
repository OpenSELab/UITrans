from core.db.model.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text


class TranslationTable(Base):
    __tablename__ = "translation_table"

    source_language: Mapped[str] = mapped_column()
    source_component: Mapped[str] = mapped_column()
    source_component_code: Mapped[str] = mapped_column(Text, nullable=False)
    source_component_description: Mapped[str] = mapped_column(Text, nullable=False)
    source_component_version: Mapped[str] = mapped_column()

    target_language: Mapped[str] = mapped_column()
    target_component: Mapped[list[str]] = mapped_column()
    target_component_code: Mapped[str] = mapped_column(Text, nullable=False)
    target_component_description: Mapped[str] = mapped_column(Text)
    target_component_version: Mapped[str] = mapped_column()

    disabled: Mapped[bool] = mapped_column(default=True)