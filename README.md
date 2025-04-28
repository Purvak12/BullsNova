<div align="center">
  <img width="200" src="static/favicon/android-chrome-512x512.png" alt="Finance Web App Logo">

# Finance: Full Stack Web App using Flask, SQLAlchemy, and Redis
</div>

---

## 📚 Project Description

Finance is a full-stack stock trading simulation platform built using **Flask**, **SQLite**, **SQLAlchemy**, and **Redis**.  
Users can register, login, lookup live stock prices, buy/sell stocks, and view their portfolio and transaction history.  
This project emulates a real-world trading application with server-side sessions, external API integrations, and database-driven dynamic content.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip (Python package installer)
- SQLite3 (comes pre-installed with Python)
- Redis Server (local or cloud instance)

---

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
2.Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Environment Variables:

Create a .env file in the root directory.

Add your Stock API key inside:

API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here

5.Initialize the Database: In a Python shell:
from application import db
db.create_all()


6.Start Redis Server (if local):

redis-server

7.Run the application:
python application.py

8.Access the application:
Open your browser and navigate to http://localhost:5000/

⚙️ Project Structure

File/Folder | Purpose
application.py | Main Flask application with all routes and configurations
helpers.py | Helper functions: API lookup, USD formatting, login_required decorator
requirements.txt | List of Python packages used
static/ | Static files (CSS, JS, images)
templates/ | HTML templates rendered by Flask
finances.db | SQLite database storing users, portfolios, transactions
Dockerfile | Instructions to containerize the application (Optional for deployment)

🧠 Features
User Authentication (Registration, Login, Logout)

Password Hashing for secure credentials storage

Real-time Stock Quote Lookup (via external API)

Buy Stocks and update Portfolio dynamically

Sell Stocks with automatic Cash adjustment

View complete Transaction History (Bought/Sold)

Custom Error Handling Pages (400, 401, 403, 404)

Session Management with Redis

Clean and responsive UI (via Jinja2 templates)

🗄️ Database Tables

Table	Columns
users	id, username, hash, cash
portfolio	id, user_id, symbol, current_shares
bought	id, buyer_id, time, symbol, shares_bought, price_bought
sold	id, seller_id, time, symbol, shares_sold, price_sold
📈 Future Improvements (Optional)
Live Stock Price Updates on Dashboard

Multi-currency support (USD, INR)

Email Notifications for transactions

OAuth login (Google, LinkedIn)

Full RESTful API backend

🛡️ Security Features
Password hashing with PBKDF2 and SHA256

Server-side session storage using Redis

CSRF prevention via Flask-WTF (optional future addition)

Environment variable based secret management

Database transactions with rollback on failure

🛠️ Tech Stack
Backend: Flask, SQLAlchemy, Marshmallow

Frontend: HTML, CSS (Bootstrap optionally)

Database: SQLite3

Session Management: Redis

External API: StockData.org

Containerization (optional): Docker

🖼️ Screenshots
(Add screenshots here if you want — like Landing Page, Portfolio, Buy/Sell pages, History page)

🔒 License
This project is intended for learning purposes only.
All rights reserved © Purvak Pal 2025.

yaml
---

# 🎯 Key Points:

- No external cloud or badge links.
- No third-party website links.
- Only internal assets (`static/favicon/android-chrome-512x512.png`) used.
- Clean, simple, highly professional — ideal for **GitHub**, **resume**, and **interviews**.
- Divides everything logically — Install, Run, Features, Security, Future Scope, etc.








