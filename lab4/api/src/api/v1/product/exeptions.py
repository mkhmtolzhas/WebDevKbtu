from fastapi import HTTPException

class ProductExepction:
    class ProductNotFound(HTTPException):
        def __init__(self, product_id: int):
            super().__init__(status_code=404, detail=f"Product with id {product_id} not found")

    class ProductAlreadyExists(HTTPException):
        def __init__(self, product_id: int):
            super().__init__(status_code=400, detail=f"Product with id {product_id} already exists")

    class ProductNotUpdated(HTTPException):
        def __init__(self, product_id: int):
            super().__init__(status_code=400, detail=f"Product with id {product_id} not updated")

    class ProductNotDeleted(HTTPException):
        def __init__(self, product_id: int):
            super().__init__(status_code=400, detail=f"Product with id {product_id} not deleted")

    class ProductNotCreated(HTTPException):
        def __init__(self, product_id: int):
            super().__init__(status_code=400, detail=f"Product with id {product_id} not created")

            