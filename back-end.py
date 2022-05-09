from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os, os.path


UPLOAD_FOLDER = 'C:/Users/Chris Telioglanidis/Desktop/Back-end/uploads' #Path to save the uploaded file
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/') #Starting path, useless for now
def hello():
    return "Hello! Go to /upload."

@app.route('/upload') #File select screen
def upload_file():
    return render_template('back-end.html')


@app.route('/uploader', methods=['GET', 'POST']) #File uploaded screen
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)
