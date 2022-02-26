from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    db = sqlite3.connect("users.db")
    cursor = db.cursor()

    name = request.form.get("name")
    if not name:
        return redirect("/")
    else:
        cursor.execute(f"""INSERT INTO users (name) VALUES("{name}"); """)
        db.commit()
        db.close()
        return render_template("register.html", name=name)

@app.route("/deregister", methods=["POST"])
def deregister():
    db = sqlite3.connect("users.db")
    cursor = db.cursor()

    db_nameQuery = cursor.execute("SELECT * FROM users;")
    for user in db_nameQuery:
        if user[0]:
            cursor.execute(f"""DELETE FROM users WHERE id = {user["id"]}; """)
            db.commit()
            db.close()
            print("Trace")
        
        return render_template("index.html")