from sqlalchemy import select
from .schemas import ProductCreate, ProductInDB, ProductUpdate
from .models import ProductModel
from sqlalchemy.ext.asyncio import AsyncSession
from .exeptions import ProductExepction

class ProductService:
    @staticmethod
    async def create_product(session: AsyncSession, product: ProductCreate) -> ProductInDB:
        try:
            new_product = ProductModel(**product.model_dump())
            session.add(new_product)
            await session.commit()
            await session.refresh(new_product)

            new_product = ProductInDB.model_validate(new_product, from_attributes=True).model_dump()

            return new_product
        except Exception:
            raise ProductExepction.ProductNotCreated
        

    @staticmethod
    async def get_products(session: AsyncSession, page: int = 1, limit: int = 10) -> list[ProductInDB]:
        try:
            stmt = select(ProductModel).limit(limit).offset((page - 1) * limit)
            result = await session.execute(stmt)
            products = result.scalars().all()

            products = [ProductInDB.model_validate(product, from_attributes=True).model_dump() for product in products]

            return products
        except Exception as e:
            raise ProductExepction.ProductNotFound

    @staticmethod
    async def get_product(session: AsyncSession, product_id: int) -> ProductInDB:
        try:
            stmt = select(ProductModel).where(ProductModel.id == product_id)
            result = await session.execute(stmt)
            product = result.scalars().first()

            if not product:
                raise ProductExepction.ProductNotFound

            product = ProductInDB.model_validate(product, from_attributes=True).model_dump()

            return product
        except Exception:
            raise ProductExepction.ProductNotFound

    @staticmethod
    async def update_product(session: AsyncSession, product_id: int, product: ProductUpdate) -> ProductInDB:
        try:
            updated_product = await session.get(ProductModel, product_id)
            if not updated_product:
                raise ProductExepction.ProductNotFound
            
            for key, value in product.model_dump(exclude_unset=True).items():
                setattr(updated_product, key, value)

            await session.commit()
            await session.refresh(updated_product)

            updated_product = ProductInDB.model_validate(updated_product, from_attributes=True).model_dump()

            return updated_product
        except Exception:
            raise ProductExepction.ProductNotUpdated
    
    @staticmethod
    async def delete_product(session: AsyncSession, product_id: int) -> bool:
        try:
            product = await session.get(ProductModel, product_id)
            if not product:
                raise ProductExepction.ProductNotFound

            await session.delete(product)
            await session.commit()

            return True
        except Exception:
            raise ProductExepction.ProductNotDeleted