from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect("mydatabase.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM returned_names")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/")
def home():
    returned_names = get_data()
    return render_template("odysseydatabase.html", returned_names=returned_names)

@app.route("/add", methods=["POST"])
def add():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    address = request.form["address"]
    city = request.form["city"]
    state = request.form["state"]
    zipcode = request.form["zipcode"]
    reason_returned = request.form["reason_returned"]

    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO returned_names (first_name, last_name, address, city, state, zipcode, reason_returned) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                   (first_name, last_name, address, city, state, zipcode, reason_returned))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
