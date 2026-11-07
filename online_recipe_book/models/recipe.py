from sqlalchemy import ForeignKey, Integer, String, Text, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Recipe(Base):
    __tablename__ = "recipes"
    __table_args__ = (
        CheckConstraint("length(name) > 0", name="ck_recipe_name_not_empty"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), index=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    ingredients: Mapped[str] = mapped_column(Text, nullable=False)
    instructions: Mapped[str] = mapped_column(Text, nullable=False)
    cuisine: Mapped[str] = mapped_column(String(60), index=True, nullable=False)
    difficulty: Mapped[str] = mapped_column(String(20), index=True, nullable=False)
    category_id: Mapped[int | None] = mapped_column(
        ForeignKey("categories.id", ondelete="SET NULL"), nullable=True, index=True
    )

    category: Mapped["Category | None"] = relationship(back_populates="recipes")
