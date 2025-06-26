# 🔐 Flask RBAC Auth – Role-Based Access Control with MySQL

A beginner-friendly backend project built with **Flask**, **MySQL**, and **Python** to demonstrate:

- ✅ User registration & login with role
- 🔐 Role-Based Access Control (RBAC)
- ⚙️ MySQL database connection using environment variables
- 📦 API-based backend, tested with Postman

---

## 📁 Project Structure

flask_rbac_auth/
├── app.py # Main Flask app
├── connection.py # MySQL connection setup
├── .env # DB credentials (excluded in .gitignore)
├── routes/
│ ├── auth.py # Register & Login routes
│ └── event.py # Event creation route (role protected)
├── models/
│ └── user.py # User model (optional logic)
├── DB_Script.sql # Sample schema
├── requirements.txt
└── venv/ # Virtual environment (excluded)


---

## ⚙️ Technologies Used

- **Python 3**
- **Flask**
- **MySQL**
- **python-dotenv**
- **Postman (for testing)**

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MuraliV1983/flask_rbac_auth.git
cd flask_rbac_auth

2. Setup Virtual Environment
bash
Copy
Edit
py -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On Linux/macOS
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Create .env file
ini
Copy
Edit
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=flask_auth_db
⚠️ Make sure your MySQL server is running and flask_auth_db is created.

🧪 API Testing Guide (Use Postman)
🔸 Register User
POST /auth/register

json
Copy
Edit
{
  "username": "adminuser",
  "password": "secret123",
  "role": "admin"
}
🔸 Login User
POST /auth/login

json
Copy
Edit
{
  "username": "adminuser",
  "password": "secret123"
}
✅ Returns login success message and sets user session.

🔸 Create Event (admin or editor only)
POST /events/create

json
Copy
Edit
{
  "title": "Python + MySQL RBAC Launch"
}
🔒 Protected by role-based access:

admin ✅

editor ✅

viewer ❌ (access denied)

📦 Sample DB Tables
See DB_Script.sql to create:

users table

events table

🙌 Author
👤 V MuraliDharan
🔗 LinkedIn – dharanv

If this project helped you, please ⭐️ star the repo and share it!

📌 Future Enhancements
Add logout route

Add JWT token support

Add event listing for all users

Add password hashing (currently plain text)

📢 Show Some ❤️
If you found this project useful or inspiring:

Share it with your team

Fork it and experiment

Tag me on LinkedIn when you post your learning!
