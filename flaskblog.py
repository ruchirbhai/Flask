# following Corey Schafer Python Flask Tutorials

from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author': 'Ruchir Sutaria',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 19, 2020'
    },
    {
        'author': 'Corey schafer',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 19, 2020'
    },
]
# app.route are decorators will handle complicated backend stuff
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
