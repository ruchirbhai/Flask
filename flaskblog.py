# following Corey Schafer Python Flask Tutorials

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'aaa30c8de284f296c1f3ae50a52cf590'

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form= form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'Success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='login', form= form)

if __name__ == '__main__':
    app.run(debug=True)
