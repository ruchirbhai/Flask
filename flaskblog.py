# following Corey Schafer Python Flask Tutorials

from flask import Flask
app = Flask(__name__)


# app.route are decorators will handle complicated backend stuff
@app.route('/')
@app.route('/home')
def home():
    return '<h1>Home Page</h1>'


@app.route('/about')
def about():
    return '<h1>About Page</h1>'

if __name__ == '__main__':
    app.run(debug=True)
