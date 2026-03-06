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
 

from fastapi import FastAPI, Query
print("THIS IS THE CORRECT FILE RUNNING")
app = FastAPI()

# ── Temporary data — acting as our database for now ──────────

products = [

    {'id': 1, 'name': 'Wireless Mouse', 'price': 499,  'category': 'Electronics', 'in_stock': True },

    {'id': 2, 'name': 'Notebook',  'price':  99,  'category': 'Stationery',  'in_stock': True },

    {'id': 3, 'name': 'USB Hub',  'price': 799, 'category': 'Electronics', 'in_stock': False},

    {'id': 4, 'name': 'Pen Set',   'price':  149, 'category': 'Stationery',  'in_stock': True },
    
    {'id': 5, 'name': 'Keyboard',  'price': 399, 'category':'Electronics','in_stock': True },
    
    {'id': 6, 'name': 'bottle',  'price':59, 'category':'Stationery','in_stock': False},
    
    {'id':7,'name':'speaker', 'price':499, 'category':'Electronics','in_stock':True},

]

 
# ── Endpoint 0 — Home ────────────────────────────────────────

@app.get('/')

def home():

    return {'message': 'Welcome to our E-commerce API'}

# ── Endpoint 1 — Return all products ──────────────────────────

@app.get('/products')

def get_all_products():

    return {'products': products, 'total': len(products)}


# To filter check below code till endpoint 2

@app.get('/products/filter')

def filter_products(

    category:  str  = Query(None, description='Electronics or Stationery'),

    max_price: int  = Query(None, description='Maximum price'),

    in_stock:  bool = Query(None, description='True = in stock only')

):

    result = products          # start with all products


    if category:

        result = [p for p in result if p['category'] == category]

    if max_price:

        result = [p for p in result if p['price'] <= max_price]

 
    if in_stock is not None:

        result = [p for p in result if p['in_stock'] == in_stock]

 

    return {'filtered_products': result, 'count': len(result)}

#  ── Endpoint 3 — Return products by category. ──────────────────

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

# ── Endpoint 2 — Return one product by its ID ──────────────────

@app.get('/products/{product_id}')

def get_product(product_id: int):

    for product in products:

        if product['id'] == product_id:

            return {'product': product}

    return {'error': 'Product not found'}


    
   

# to run this do  below

# To start - venv\Scripts\activate
# to run it  -  uvicorn main2:app --reload

# and to get products  -> http://127.0.0.1:8000/products    write product and for specific mention id 


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

# post in next day on 6th march
