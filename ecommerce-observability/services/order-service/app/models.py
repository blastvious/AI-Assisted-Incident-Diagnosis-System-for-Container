from sqlalchemy import String, Integer, Numeric

from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    customer_name: Mapped[str] = mapped_column(String(100))

    product_name: Mapped[str] = mapped_column(String(100))

    quantity: Mapped[int] = mapped_column(Integer)

    total_price: Mapped[float] = mapped_column(Numeric(10,2))

    status: Mapped[str] = mapped_column(String(50), default="PENDING")

    