🚀 FastAPI Internship Practice — IN226014802
This project is part of my FastAPI internship where I built a backend system step by step. The main goal was to understand how real-world APIs work by creating a product and order management system.
Instead of jumping directly into complex systems, I started with basic APIs and gradually added features like search, sorting, pagination, and order processing.
💡 Everything is built using FastAPI with in-memory data (no database), so the focus is purely on backend logic and API design.
________________________________________
⚙️ Setup
1️⃣ Install dependencies
pip install fastapi uvicorn
2️⃣ Activate virtual environment
venv\Scripts\activate
3️⃣ Run the server
uvicorn main:app --reload
4️⃣ Open Swagger UI
http://127.0.0.1:8000/docs
________________________________________
📌 Features & Implementation
________________________________________
🛒 1. Product Management (CRUD)
I created APIs to manage products:
•	Add product
•	View all products
•	Update product
•	Delete product
📌 Example (Real-world):
Like Amazon admin panel → you add a product with:
•	Name: iPhone 13
•	Price: ₹60,000
•	Category: Mobile
________________________________________
🔍 2. Search (Case-Insensitive)
Users can search products without worrying about uppercase/lowercase.
📌 Example (Real-world):
•	User types: iphone
•	System returns: iPhone, IPHONE, Iphone
👉 Same behavior as Amazon/Flipkart search.
________________________________________
🔃 3. Sorting
Products can be sorted dynamically.
📌 Options:
•	Sort by price → low to high
•	Sort by name → A to Z
📌 Example (Real-world):
On shopping apps:
•	“Price: Low to High”
•	“Name: A to Z”
👉 Same logic implemented in backend.
________________________________________
🧠 4. Advanced Sorting (Multi-Level)
Custom sorting logic:
•	First → group by category
•	Then → sort by price inside each category
📌 Example (Real-world):
E-commerce site:
•	Electronics → sorted by price
•	Clothing → sorted by price
________________________________________
📄 5. Pagination
Large data is divided into pages.
📌 Example (Real-world):
Google search results:
•	Page 1 → first results
•	Page 2 → next results
👉 Same concept used:
•	page=1&limit=5
•	page=2&limit=5
________________________________________
🔗 6. Combined API (Search + Sort + Pagination)
Single API handles multiple operations together.
📌 Example (Real-world):
User searches:
search=phone&sort_by=price&page=1
👉 Backend:
•	Filters → “phone”
•	Sorts → by price
•	Returns → page 1
________________________________________
📦 7. Order Management System
Users can place orders using product IDs.
📌 Features:
•	Validate product exists
•	Check stock availability
•	Calculate total price automatically
📌 Example (Real-world):
Like ordering on Flipkart:
•	Add 2 products
•	Total price calculated automatically
________________________________________
🔎 8. Order Search
Search orders by customer name (case-insensitive)
📌 Example:
•	Input: rahul
•	Matches: Rahul, RAHUL
________________________________________
⚠️ 9. Error Handling
Handled common backend issues:
•	Invalid input
•	Product not found
•	Out of stock
•	Wrong query parameters
📌 Example (Real-world):
•	“Product not found”
•	“Out of stock”
👉 Same responses you see on real apps.
________________________________________
🧠 Key Concepts Covered
•	FastAPI routing & endpoint design
•	Query parameters & validation
•	Pydantic models
•	CRUD operations
•	Search, sorting, pagination
•	Business logic handling
•	Error handling
________________________________________
🎯 Highlights
•	Clean and simple backend structure
•	Step-by-step implementation
•	Real-world API features
•	Easy testing using Swagger UI
•	Reusable and maintainable code
________________________________________
👨‍💻 Author
Kalpesh Sarsambe
FastAPI Internship Practice — IN226014802
________________________________________
🚀 Future Improvements
•	Add database (PostgreSQL / MongoDB)
•	Add authentication (JWT)
•	Deploy on cloud (AWS / Render)
•	Add unit testing

