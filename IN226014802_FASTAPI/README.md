# 🚀 FastAPI Internship Practice — IN226014802

This project is part of my FastAPI internship where I built a backend system step by step.  
The goal was to understand how real-world APIs work by creating a **product and order management system**.

- Started with basic APIs  
- Gradually added search, sorting, pagination  
- Implemented order management system  
- Focused on backend logic using FastAPI  
- Used in-memory data (no database)


## ⚙️ Setup

- Install dependencies:
```
pip install fastapi uvicorn

Activate virtual environment:

venv\Scripts\activate

Run the server:

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs
```

📌 Features & Implementation
🛒 1. Product Management (CRUD)

-	Add product
-	View all products
-	Update product
-	Delete product

Real-world example:
- Like Amazon admin panel
- Add product → Name: iPhone 13, Price: ₹60,000, Category: Mobile
________________________________________
🔍 2. Search (Case-Insensitive)
- Search works without uppercase/lowercase issues
Example:
- iphone → matches iPhone, IPHONE, Iphone
- Same behavior as Amazon / Flipkart search
________________________________________
🔃 3. Sorting
- Sort by price → low to high
- Sort by name → A to Z
Example:
- Shopping apps filter → “Price: Low to High”
________________________________________
🧠 4. Advanced Sorting (Multi-Level)
- First group products by category
- Then sort by price inside each category
Example:
- Electronics → sorted by price
- Clothing → sorted by price
________________________________________
📄 5. Pagination
- Split large data into pages
Example:
- page=1&limit=5 → first 5 products
- page=2&limit=5 → next 5 products
- Same concept as Google search pages
________________________________________
🔗 6. Combined API (Search + Sort + Pagination)
- Single API handles multiple operations
Example:
search=phone&sort_by=price&page=1
- Backend flow:
- Filter → "phone"
- Sort → price
- Return → page 1
________________________________________
📦 7. Order Management System
- Place orders using product IDs
- Validate product exists
- Check stock availability
- Calculate total price automatically
Example:
- Like Flipkart:
- Add 2 products
- Total price auto-calculated
________________________________________
🔎 8. Order Search
- Search orders by customer name
- Case-insensitive
Example:
- kalpesh → matches kalpesh, KALPESH
________________________________________
⚠️ 9. Error Handling
- Invalid input
- Product not found
- Out of stock
- Wrong query parameters
Example:
- “Product not found”
- “Out of stock”
________________________________________
🧠 Key Concepts Covered
- FastAPI routing & endpoint design
- Query parameters & validation
- Pydantic models
- CRUD operations
- Search, sorting, pagination
- Business logic handling
- Error handling
________________________________________
🎯 Highlights
- Clean and simple backend structure
- Step-by-step implementation
- Real-world API features
- Easy testing using Swagger UI
- Reusable and maintainable code
________________________________________
👨‍💻 Author
Kalpesh Sarsambe
- FastAPI Internship Practice — IN226014802


