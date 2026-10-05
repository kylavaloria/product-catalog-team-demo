from fastapi import FastAPI

from app.data import PRODUCTS

app = FastAPI(title="Product Catalog Demo")


@app.get("/products")
def list_products(in_stock_only: bool = False) -> list[dict]:
    """Return products in catalog order, optionally limited to in-stock items."""
    if in_stock_only:
        return [product for product in PRODUCTS if product["in_stock"]]
    return PRODUCTS
