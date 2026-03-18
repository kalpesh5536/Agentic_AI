🚀 FastAPI Internship Practice — IN226014802

This project is part of my FastAPI internship where I built a backend system step by step. The goal was to understand how real-world APIs work by creating a product and order management system.

I started with basic APIs and then gradually added features like search, sorting, pagination, and order handling. Everything is built using FastAPI and uses in-memory data (no database), just to focus on logic and API design.

⚙️ Setup

Install required packages:

pip install fastapi uvicorn

Activate virtual environment:

venv\Scripts\activate

Run the server:

uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000/docs
📌 What I Built
1. Product Management

I created APIs to manage products (add, view, update, delete).

Example:

Add a product → name, price, category

Get all products → returns list

2. Search (Case-Insensitive)

Users can search products by name without worrying about uppercase/lowercase.

Example:

Searching "laptop" will match "Laptop" or "LAPTOP"

3. Sorting

Products can be sorted by fields like price or name.

Example:

Sort by price (low to high)

Sort by name (A to Z)

Validation is added to prevent invalid sorting fields.

4. Advanced Sorting (Multi-Level)

Custom logic:

First group products by category

Then sort each category by price

5. Pagination

Data is split into pages for better performance.

Example:

Page 1 → first 5 products

Page 2 → next 5 products

6. Combined API (Search + Sort + Pagination)

Single API that supports multiple operations.

Example:

search=phone

sort_by=price

page=1

7. Order Management System

Users can place orders by selecting products.

Features:

Validate product existence

Check stock availability

Auto-calculate total price

8. Order Search

Search orders by customer name (case-insensitive).

Example:

"rahul" matches "Rahul"

9. Error Handling

Handled cases like:

Invalid inputs

Product not found

Out of stock

Wrong query parameters

🧠 What I Learned

FastAPI routing and API design

Query parameters and validation

Pydantic models

CRUD operations

Search, sorting, pagination

Backend logic handling

🎯 Highlights

Clean and simple backend structure

Step-by-step implementation

Real-world API features

Easy testing using Swagger UI

Reusable and maintainable code

👨‍💻 Author

Kalpesh Sarsambe
FastAPI Internship Practice — IN226014802
