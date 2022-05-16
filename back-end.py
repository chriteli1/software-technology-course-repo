from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os, os.path
import json
from urllib.request import urlopen


#UPLOAD_FOLDER = 'C:/Users/Chris Telioglanidis/Desktop/Back-end/uploads' #Path to save the json file
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/') #Starting path, useless for now
def hello():
    return "Hello! Go to /upload."

@app.route('/upload') #Url input screen
def upload_file():
    return render_template('back-end.html')


@app.route('/uploader', methods=['POST', 'GET']) #Url sent screen
def uploader():
    if request.method == 'POST':
        f = request.form['url']
        with urlopen(f) as response:
            source = response.read()
        #f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        data = json.loads(source)
    return 'File uploaded successfully.'


if __name__ == '__main__':
    app.run(debug=True)
