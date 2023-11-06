from flask import Flask, render_template, request 
import sqlite3 
import threading
app=Flask(__name__)

connection = sqlite3.connect("Intermediate_flask-2.db")
cursor=connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Products
(product_id INTEGER PRIMARY KEY AUTOINCREMENT, product TEXT,
price_per_tonne INT)
''')

productsToInsert = [
    ('Bananas', 7000),
    ('Avacados', 12000),
    ('Tomatos', 3100)
]

cursor.executemany('''
                   INSERT INTO Products(product,price_per_tonne)
                   VALUES (?,?)
                   ''',productsToInsert)

@app.route("/")
def open():
    return render_template("Intermediate_flask-2.1.html")

@app.route("/crud",methods=['POST','GET'])
def sel():
    name=request.form.get("name")
    if name == "read":
        cursor.execute("SELECT * FROM Products")
        results = cursor.fetchall()
        print("Results in thread:", threading.current_thread().name)
        for row in results:
            print(row)
    elif name == "update":
        @app.route("/cl",methods=['POST','GET'])
        def vp():
            return render_template("Intermediate_flask-2.2.html")
            value=request.form.get("value")
            product=request.form.get("product")
            cursor.execute("UPDATE Products SET price_per_tonne = ? WHERE product=?",value,product)
            return f"Table Updated Successfully."

connection.commit()
connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)

    threads = []
    for i in range(3):
        thread = threading.Thread(target=thread_function)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()