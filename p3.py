from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xxxxxx'
app.config['MYSQL_DB'] = 'crud_db'

mysql = MySQL(app)

# READ (Display Data)
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template("index.html", users=data)

# CREATE (Insert Data)
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    return render_template("add.html")

# UPDATE
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, id))
        mysql.connection.commit()
        return redirect('/')
    cur.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cur.fetchone()
    return render_template("edit.html", user=user)

# DELETE
@app.route('/delete/<int:id>')
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


    
