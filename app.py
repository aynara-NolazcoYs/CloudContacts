from flask import Flask, render_template, request, redirect
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form.get("phone", "")

    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        # Validar si el correo ya existe
        cursor.execute("SELECT * FROM contacts WHERE email = %s", (email,))
        existing = cursor.fetchone()
        if existing:
            return render_template("index.html", error="El correo ya está registrado.")

        # Insertar nuevo contacto
        sql = "INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, phone))
        db.commit()

    except mysql.connector.Error as err:
        return render_template("index.html", error=f"Error al conectar con la base de datos: {err}")

    finally:
        cursor.close()
        db.close()

    return redirect("/contacts")

@app.route("/contacts")
def contacts():
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contacts ORDER BY created_at DESC")
        data = cursor.fetchall()
    except mysql.connector.Error as err:
        return f"Error al consultar la base de datos: {err}"
    finally:
        cursor.close()
        db.close()

    return render_template("contacts.html", contacts=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

