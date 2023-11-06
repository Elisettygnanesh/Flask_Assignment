from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def open_site():
    return render_template('Basic_flask-4.html')

@app.route("/empsite",methods=['POST','GET'])
def emp_det():
    name=request.form.get('name')
    empid=request.form.get('empid')
    salary=request.form.get('salary')
    emailid=request.form.get('emailid')
    des=request.form.get('des')
    return f"Employee Name: {name}\nEmployee Empid: {empid}\nEmployee Salary: {salary}\nEmployee Emailid: {emailid}\nEmployee Designation: {des}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)