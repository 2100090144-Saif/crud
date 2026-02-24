📘 Flask CRUD Application with MySQL
This is a simple CRUD web application built using Flask and MySQL.
The project allows users to add, view, update, and delete records from a MySQL database.

I created this project to understand how Flask connects with MySQL and how CRUD operations work in a real web application.

What This Project Does
--Add a new user (name and email)

--View all users in a table

--Edit existing user details

--Delete users from the database

--Connect Flask with MySQL using flask-mysqldb

Technologies Used

Python
Flask
MySQL
flask-mysqldb
HTML 


🗄 Database Setup

1️⃣ Create Database
CREATE DATABASE crud_db;
USE crud_db;

2️⃣ Create Table

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

⚙️ Installation & Setup

1️⃣ Clone Projectgit 
clone <your-repo-link>
cd flask-crud-app

2️⃣  Create Virtual Environment (Recommended)
python -m venv venv

Activate:
Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

3️⃣ Install Requirements
pip install flask flask-mysqldb

4️⃣ Configure MySQL in app.py
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'crud_db'

5️⃣ Run Application
python app.py

Open browser:
http://127.0.0.1:5000/


📸 Application Pages

🏠 Home Page
   Displays all users
   Edit & Delete options

➕ Add User Page
   Form to insert new user

✏️ Edit User Page
   Update existing user details




































