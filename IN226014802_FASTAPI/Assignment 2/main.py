"""
from fastapi import FastAPI
app= FastAPI()
@app.get("/")   # decorator
def home():
    return {"message": "Welcome to our app"}
"""
# To start - venv\Scripts\activate
# to run it is -  uvicorn main:app --reload



# Http: methods; the language of APIs

# 1) GET - fetch/read data from server
# ex. - want to see all products from e-commerce

# 2) POST - Create/ submit

# 3) PUT - Update/ replace data on the server

# 4) DELETE -  removes/ deletes from our connection
 
# JSON - java script object notation
# it is in the form { key : value}- dictionary format 

# end point, routing will be in day2

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Fast API Day 2

# GET- end points, swagger UI, path parameter, query parameter, post request

#   Add some real world business data + GET EndPoints
# how it shows details of amazon products 
 
# day 1
from fastapi import FastAPI, Query

# For day 2
from typing import Optional, List
from pydantic import BaseModel, Field


app = FastAPI()

# ── Temporary data — acting as our database for now ──────────

products = [

    {'id': 1, 'name': 'Wireless Mouse', 'price': 99,  'category': 'Electronics', 'in_stock': True },

    {'id': 2, 'name': 'Notebook',  'price':  99,  'category': 'Stationery',  'in_stock': True },

    {'id': 3, 'name': 'USB Hub',  'price': 799, 'category': 'Electronics', 'in_stock': False},

    {'id': 4, 'name': 'Pen Set',   'price':  149, 'category': 'Stationery',  'in_stock': True },
    
    {'id': 5, 'name': 'Keyboard',  'price': 399, 'category':'Electronics','in_stock': True },
    
    {'id': 6, 'name': 'bottle',  'price':59, 'category':'Stationery','in_stock': False},
    
    {'id':7,'name':'speaker', 'price':899, 'category':'Electronics','in_stock':True},
    
    

]

# DAY 1 ENDPOINTS
# ── Endpoint 0 — Home ────────────────────────────────────────

@app.get('/')

def home():

    return {'message': 'Welcome to our E-commerce API'}

# ── Endpoint 1 — Return all products ──────────────────────────

# Q1 — Show all products
@app.get('/products')

def get_all_products():
    return {'products': products, 'total': len(products)}

# To filter check below code till endpoint 2

@app.get('/products/filter')

def filter_products(

    category:  str  = Query(None, description='Electronics or Stationery'),

    max_price: int  = Query(None, description='Maximum price'),
    
# Day 2, Q1)  Filter Products by Minimum Price

    min_price: int = Query(None, description= 'Minimum price'),

    in_stock:  bool = Query(None, description='True = in stock only')

):
    result = products          # start with all products


    if category:

        result = [p for p in result if p['category'] == category]

    if max_price :

        result = [p for p in result if p['price'] <= max_price]
    
    if min_price :
         
        result = [p for p in result if p['price']>= min_price]
 
    if in_stock is not None:

        result = [p for p in result if p['in_stock'] == in_stock]
        
    return {'filtered_products': result, 'count': len(result)}

#  ── Endpoint 3 — Return products by category. ──────────────────

# Q2 — Filter by category
@app.get("/products/category/{category_name}")

def get_products_by_category(category_name: str):
    
    filtered= []
    
    for product in products:
        if product['category'].lower()== category_name.lower():
            filtered.append(product)
    
    if not filtered:
        return {"error": "No products found in this category"}
    
    return {"products": filtered}


# ── Endpoint 4 — Return in stock items only ──────────────────

# Q3 — Only in-stock products

@app.get("/products/in_stock")
def get_in_stock_products():
    
    in_stock_products = []
    
    for product in products:
        if product["in_stock"]== True:
            in_stock_products.append(product)
            
    return{
        "in_stock_products": in_stock_products,
        "count": len(in_stock_products)
    }
            
            
# ── Endpoint 5 — Return summary i,e Store Info ──────────────────
# Q4 — Store summary

@app.get("/store/summary")
def store_summary():
    
    total_products =len(products)
    
    in_stock =0
    out_of_stock=0
    categories =set()
    
    for product in products:
        categories.add(product["category"])
        
        if product["in_stock"]:
            in_stock+=1
        else:
            out_of_stock+=1
    return{
        "store_name":"My E-commerce store",
        "total_products": total_products,
        "in_stock": in_stock,
        "out_of_stock":out_of_stock,
        "categories":list(categories)
    }
    

 # ── Endpoint 7 -- Cheapest & Most Expensive Product API ──────
 
 # ⭐ BONUS — Best deal and premium pick
 
@app.get("/products/deals")
def product_deals():
    
    cheapest_product = products[0]
    expensive_product = products[0]
    
    for product in products:
        
        if product["price"]< cheapest_product["price"]:
            cheapest_product =product
            
        if product["price"]> expensive_product["price"]:
            expensive_product= product
    return {
        "Best deal":cheapest_product,
        "Premium product":expensive_product
    }
    
# ── Endpoint 6 -- Search Products by Name ──────────────────


# Q5 — Search products
@app.get('/products/search/{keyword}')
def search_products(keyword: str):
    matched_products=[]
    
    for product in products:
        if keyword.lower() in product["name"].lower():
            matched_products.append(product)
    
    if not matched_products:
        return {"message": "No products matched you search"}
    
    return{
        "matched_products":matched_products,
        "count": len(matched_products)
    }




#  to get products  -> http://127.0.0.1:8000/products    write product and for specific mention id 


# 2) Swagger UI - vs code automatically makes doc , i,e full visual interface to test your API
 # http://127.0.0.1:8000/docs   just write /docs
 
 
# 3) Query Parameters : Filter products or data
# only for electronics which are less than 300 etc

# This is a extra info --> URL after we execute
# http://127.0.0.1:8000/products?  write Question mark after products and write category= Electronics, see below
#1)  http://127.0.0.1:8000/products/filter?category=Electronics
 
#2) http://127.0.0.1:8000/products/filter?category=Stationery
# 3) http://127.0.0.1:8000/products/filter?category=Electronics&max_price=600
# 4) http://127.0.0.1:8000/products/filter? in_stock=True

# post in next day on 9th march


# Day 2 of FastAPI

# get only used to read or fetch, just a url

# Post - Request + Pydantic  model, send or to create data, not a url, check in swagger UI
# Pydantic model - to validate, it is used, to make compulsory to specific field


# ---------------------------------------------------------
# DAY 2 PRACTICE TASKS 
# ---------------------------------------------------------

# Day 2 - Task 1: Filter Products by Minimum Price is written above check in day 1 filter.




# Day 2 - Task 3: Pydantic + POST - Accept Customer Feedback
class CustomerFeedback(BaseModel):
    customer_name: str = Field(min_length=2)
    product_id: int = Field(gt=0)
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = Field(default=None, max_length=300)

feedback_list = []

@app.post("/feedback")
def submit_feedback(feedback: CustomerFeedback):
    feedback_list.append(feedback.model_dump())
    return {
        "message": "Feedback submitted successfully",
        "feedback": feedback.model_dump(),
        "total_feedback": len(feedback_list)
    }


# Day 2 - Task 4: Build a Product Summary Dashboard
@app.get("/products/summary")
def get_products_summary():
    in_stock_count = sum(1 for p in products if p["in_stock"])
    out_of_stock_count = len(products) - in_stock_count
    
    sorted_products = sorted(products, key=lambda x: x["price"])
    cheapest = {"name": sorted_products[0]["name"], "price": sorted_products[0]["price"]}
    most_expensive = {"name": sorted_products[-1]["name"], "price": sorted_products[-1]["price"]}
    
    # Extract unique categories
    categories = list(set(p["category"] for p in products))
    
    return {
        "total_products": len(products),
        "in_stock_count": in_stock_count,
        "out_of_stock_count": out_of_stock_count,
        "most_expensive": most_expensive,
        "cheapest": cheapest,
        "categories": categories
    }

# Day 2 - Task 5: Validate & Place a Bulk Order

class OrderItem(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., ge=1, le=50)

class BulkOrder(BaseModel):
    company_name: str = Field(..., min_length=2)
    contact_email: str = Field(..., min_length=5)
    items: List[OrderItem] = Field(min_items=1)

@app.post("/orders/bulk")
def bulk_order(order: BulkOrder):

    confirmed = []
    failed = []
    grand_total = 0

    for item in order.items:

        product = next((p for p in products if p["id"] == item.product_id), None)

        if not product:
            failed.append({
                "product_id": item.product_id,
                "reason": "Product not found"
            })
            continue

        if not product["in_stock"]:
            failed.append({
                "product_id": item.product_id,
                "reason": f"{product['name']} is out of stock"
            })
            continue

        subtotal = product["price"] * item.quantity
        grand_total += subtotal

        confirmed.append({
            "product": product["name"],
            "qty": item.quantity,
            "subtotal": subtotal
        })

    return {
        "company": order.company_name,
        "confirmed": confirmed,
        "failed": failed,
        "grand_total": grand_total
    }

orders = []

class Order(BaseModel):
    product_id: int
    quantity: int


# Day 2 - ⭐ Bonus: Order Status Tracker
class SingleOrder(BaseModel):
    product_id: int
    quantity: int

orders_db = []
order_id_counter = 1

@app.post("/orders")
def create_order(order: SingleOrder):
    global order_id_counter
    
    new_order = {
        "order_id": order_id_counter,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "status": "pending"
    }
    
    orders_db.append(new_order)
    order_id_counter += 1
    return new_order

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders_db:
        if order["order_id"] == order_id:
            return order
    return {"error": "Order not found"}

@app.patch("/orders/{order_id}/confirm")
def confirm_order(order_id: int):
    for order in orders_db:
        if order["order_id"] == order_id:
            order["status"] = "confirmed"
            return {"message": "Order confirmed successfully", "order": order}
            
    return {"error": "Order not found"}


# Day 2 - Task 2: Get Only the Price of a Product
@app.get("/products/{product_id}/price")
def get_product_price(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {"name": product["name"], "price": product["price"]}
    return {"error": "Product not found"}


# ── Endpoint 2 — Return one product by its ID ──────────────────

@app.get('/products/{product_id}')

def get_product(product_id: int):

    for product in products:

        if product['id'] == product_id:

            return {'product': product}

    return {'error': 'Product not found'}
