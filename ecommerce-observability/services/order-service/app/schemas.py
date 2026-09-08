from pydantic import BaseModel

class OrderCreate(BaseModel):
    customer_name: str

    product_name: str

    quantity: int

    total_price: float

class OrderStatusUpdate(BaseModel):
    id: int
    customer_name: str

    product_name: str

    quantity: int

    total_price: float

    status: str

    model_config = {
        "from_attributes": True
    }