from flask import Flask, render_template, abort

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('Intermediate_flask-5_404.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('Intermediate_flask-5_500.html')

@app.route('/')
def index():
    return "Hello, User WELCOME!"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
