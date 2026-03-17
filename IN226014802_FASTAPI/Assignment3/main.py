from fastapi import FastAPI, HTTPException, Query, Response, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Existing products
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True}
]


# Model for new product
class NewProduct(BaseModel):
    name: str
    price: int
    category: str
    in_stock: bool = True

@app.get('/')

def home():

    return {'message': 'Welcome to Assignment 3'}
# --------------------------------------------------
# GET all products
# --------------------------------------------------
@app.get("/products")
def get_products():
    return products


# --------------------------------------------------
# POST add new product
# --------------------------------------------------
@app.post("/products", status_code=201)
def add_product(product: NewProduct):

    # Check duplicate product name
    for p in products:
        if p["name"].lower() == product.name.lower():
            raise HTTPException(
                status_code=400,
                detail="Product with this name already exists"
            )

    # Auto-generate ID safely
    new_id = max(p["id"] for p in products) + 1

    new_product = {
        "id": new_id,
        "name": product.name,
        "price": product.price,
        "category": product.category,
        "in_stock": product.in_stock
    }

    products.append(new_product)

    return {
        "message": "Product added",
        "product": new_product
    }


# --------------------------------------------------
# Q5 - Inventory audit
# --------------------------------------------------
@app.get("/products/audit")
def product_audit():

    in_stock_list = [p for p in products if p["in_stock"]]
    out_stock_list = [p for p in products if not p["in_stock"]]

    stock_value = sum(p["price"] * 10 for p in in_stock_list)

    priciest = max(products, key=lambda p: p["price"])

    return {
        "total_products": len(products),
        "in_stock_count": len(in_stock_list),
        "out_of_stock_names": [p["name"] for p in out_stock_list],
        "total_stock_value": stock_value,
        "most_expensive": {
            "name": priciest["name"],
            "price": priciest["price"]
        }
    }


# --------------------------------------------------
# BONUS - Apply category discount
# --------------------------------------------------
@app.put("/products/discount")
def bulk_discount(
    category: str = Query(..., description="Category to discount"),
    discount_percent: int = Query(..., ge=1, le=99, description="Discount percent")
):

    updated = []

    for p in products:
        if p["category"] == category:
            p["price"] = int(p["price"] * (1 - discount_percent / 100))
            updated.append(p)

    if not updated:
        return {"message": f"No products found in category: {category}"}

    return {
        "message": f"{discount_percent}% discount applied to {category}",
        "updated_count": len(updated),
        "updated_products": updated
    }


# --------------------------------------------------
# GET single product
# --------------------------------------------------
@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")


# --------------------------------------------------
# PUT update product
# --------------------------------------------------
@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    in_stock: Optional[bool] = Query(None),
    price: Optional[int] = Query(None)
):

    for product in products:

        if product["id"] == product_id:

            if in_stock is not None:
                product["in_stock"] = in_stock

            if price is not None:
                product["price"] = price

            return {
                "message": "Product updated",
                "product": product
            }

    raise HTTPException(status_code=404, detail="Product not found")


# --------------------------------------------------
# DELETE product
# --------------------------------------------------
@app.delete("/products/{product_id}")
def delete_product(product_id: int, response: Response):

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {"message": f"Product '{product['name']}' deleted"}

    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "Product not found"}