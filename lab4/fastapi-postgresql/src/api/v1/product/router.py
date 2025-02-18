from fastapi import APIRouter
from .service import ProductService
from .schemas import ProductCreate, ProductInDB, ProductUpdate
from src.database import SessionDependency

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/")
async def create_product(product: ProductCreate, session: SessionDependency = SessionDependency()):
    result = await ProductService.create_product(session, product)
    return {
        "message": "Product created successfully",
        "product": result
    }

@router.get("/")
async def get_products(page: int = 1, limit: int = 10, session: SessionDependency = SessionDependency()):
    result = await ProductService.get_products(session, page, limit)
    return {
        "message": "Products retrieved successfully",
        "product": result
    }

@router.get("/search")
async def get_products_by_title(title: str, page: int = 1, limit: int = 10, session: SessionDependency = SessionDependency()):
    result = await ProductService.get_products_by_title(session, title, page, limit)
    return {
        "message": "Products retrieved successfully",
        "product": result
    }

@router.get("/{product_id}")
async def get_product(product_id: int, session: SessionDependency = SessionDependency()):
    result = await ProductService.get_product(session, product_id)
    return {
        "message": "Product retrieved successfully",
        "product": result
    }

@router.put("/{product_id}")
async def update_product(product_id: int, product: ProductUpdate, session: SessionDependency = SessionDependency()):
    result = await ProductService.update_product(session, product_id, product)
    return {
        "message": "Product updated successfully",
        "product": result
   }

@router.delete("/{product_id}")
async def delete_product(product_id: int, session: SessionDependency = SessionDependency()):
    result = await ProductService.delete_product(session, product_id)
    return {
        "message": "Product deleted successfully",
        "product": result
    }
