# 🚀 FastAPI Internship Practice — IN226014802

This project is part of my FastAPI internship where I built a backend system step by step. The goal was to understand how real-world APIs work by creating a product and order management system.

I started with basic APIs and then slowly added more features like search, sorting, pagination, and order handling. Everything is built using FastAPI and uses in-memory data (no database), just to focus on logic and API design.

## Setup

Install required packages:  pip install fastapi uvicorn

Activate virtual environment: venv\Scripts\activate

Run the server: uvicorn main:app --reload


##  What I Built

### 1. Product Management

I created APIs to manage products (add, view, update, delete).

Example:

* Add a product → name, price, category
* Get all products → returns list

---

### 2. Search (Case-Insensitive)

Users can search products by name without worrying about uppercase/lowercase.

Example:

* Searching `"laptop"` will also match `"Laptop"` or `"LAPTOP"`

---

### 3. Sorting

Products can be sorted by fields like price or name.

Example:

* Sort by price (low to high)
* Sort by name (A to Z)

Also added validation so invalid fields don’t break the API.

---

### 4. Advanced Sorting (Multi-Level)

I also created custom logic where:

* First group products by category
* Then sort each category by price

This shows how real systems handle complex sorting.

---

### 5. Pagination

Instead of showing all data at once, I split it into pages.

Example:

* Page 1 → first 5 products
* Page 2 → next 5 products

This is useful when data becomes large.

---

### 6. Combined API (Search + Sort + Pagination)

I created one API where all operations work together.

Example:

* Search = "phone"
* Sort = price
* Page = 1

This is how real backend APIs are designed.

---

### 7. Order Management System

Users can place orders by selecting products.

Features:

* Check if product exists
* Check stock availability
* Calculate total price automatically

Example:

* Order: 2 items → total price calculated

---

### 8. Order Search

Orders can be searched by customer name (case-insensitive).

Example:

* `"rahul"` will match `"Rahul"`

---

### 9. Error Handling

I handled common issues like:

* Invalid inputs
* Product not found
* Out of stock
* Wrong query parameters

So the API doesn’t crash and gives proper messages.

---

## 🧠 What I Learned

* How FastAPI works (routes, endpoints)
* Using query parameters
* Data validation using Pydantic
* CRUD operations
* Writing clean API logic
* Handling real-world scenarios (search, sort, pagination)
* Basic backend architecture

---

## 🎯 Highlights

* Simple and clean code structure
* Built step-by-step (easy to understand)
* Covers real-world API features
* Easy to test using Swagger UI
* Logic is reusable and maintainable

---

## 👩‍💻 Author

Kalpesh Sarsambe
FastAPI Internship Practice — IN226014802
Assignments 1–5 completed

