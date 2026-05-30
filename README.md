# Personal Expense Tracker

A web-based financial management application built using Python and the Django framework. This project allows users to log and monitor day-to-day expenditures efficiently by managing amounts and spending categories.

## 🚀 Features
* **Expense Logging:** Add expenses with detailed parameters including Title, Amount (with currency representation), and Category.
* **Dynamic Data Flow:** Retrieves all stored financial data and displays them instantly on the dashboard.
* **Secure Submission:** Uses Django's native CSRF token security layer for all form submissions to safeguard user data entry.
* **Persistent Storage:** Integrated with an SQL backend to keep financial records saved across sessions.

## 🛠️ Tech Stack
* **Backend:** Python, Django Framework
* **Frontend:** HTML5, CSS3
* **Database:** SQLite (Default Django SQL Database)
* **Version Control:** Git & GitHub

## 📝 How to Run Locally
1. Clone this repository.
2. Run database migrations: `python manage.py migrate`.
3. Start the development server: `python manage.py runserver`.
4. Open `http://127.0.0.1:8000/` in your browser.
