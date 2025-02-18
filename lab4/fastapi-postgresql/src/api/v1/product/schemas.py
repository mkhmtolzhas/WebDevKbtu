from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str
    price: int
    description: str
    category: str
    link: str
    rating: float
    image: str

    class Config:
        from_attributes = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductInDB(ProductBase):
    id: int