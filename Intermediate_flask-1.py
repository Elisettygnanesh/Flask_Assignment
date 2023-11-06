from flask import Flask, render_template, request, redirect 
import os 
app = Flask(__name__)

save_dir="uploads/"
if not os.path.exists(save_dir):
  os.makedirs(save_dir)

@app.route('/')
def index():
  return render_template('Intermediate_flask-1.html')

@app.route("/upload", methods=["POST"])
def upload():
    # Check if the POST request has a file attached
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    # Check if the file is selected
    if file.filename == '':
        return "No selected file"

    # Save the file
    file.save(os.path.join(save_dir, "Abhi.jpg"))
    return "Your file has been submitted successfully"


if __name__ == "__main__":
  app.run(host="0.0.0.0",port=5000)