from fastapi import FastAPI

from app.data import PRODUCTS

app = FastAPI(title="Product Catalog Demo")


@app.get("/products")
def list_products() -> list[dict]:
    """Return every product in catalog order."""
    return PRODUCTS
