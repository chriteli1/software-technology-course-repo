from flask import Flask, render_template
from back_end import back_end
from api import api


app = Flask(__name__)
app.register_blueprint(back_end)
app.register_blueprint(api)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('app.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
