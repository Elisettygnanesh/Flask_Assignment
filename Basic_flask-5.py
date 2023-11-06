from flask import Flask, render_template, request
import requests
app=Flask(__name__)

@app.route("/")
def open_sel():
    return render_template("Basic_flask-5.html")

@app.route("/display",methods=['POST'])
def ds():
    name=request.form.get('name')
    accnum=request.form.get('accnum')
    bal=request.form.get('bal')
    store=request.form.get('str')
    display=request.form.get('dis')
    if store == 'yes' and display == 'no':
        return f"Thank you for filling this form. Your details are successfully stored."
    else:
        return f"Account Holder Name: {name}    Account Number: {accnum}    Available Balance: {bal}"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)