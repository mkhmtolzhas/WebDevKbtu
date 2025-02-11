from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class ProductModel(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]
    category: Mapped[str]
    link: Mapped[str]
    rating: Mapped[float]
    image: Mapped[str]

