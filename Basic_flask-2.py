from flask import Flask, render_template,request
app=Flask(__name__)

@app.route("/")
def open_add():
    return render_template("Basic_flask-2.html")

@app.route("/addapp",methods=['POST'])
def add():
    n1=request.form['num1']
    n2=request.form['num2']
    a=int(n1)+int(n2)
    return f"Addition of {n1} and {n2} is {a}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5002)