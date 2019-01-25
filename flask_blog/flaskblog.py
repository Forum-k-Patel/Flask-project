from flask import Flask, render_template, url_for, flash, redirect
from forms import RegForm, Login
from jinja2 import Environment, FileSystemLoader, loopcontrol
app = Flask(__name__)


app.config['SECRET_KEY']='bfde83bf41037a9249e2cbac7d16c51c'
posts = [

	{
		'author': 'j.k rowlings',
		'title': 'blog post 1',
		'content':'first post content',
		'date_posted':'april 20, 2018'
	},
	{
	'author':'joe doe',
	'title': 'blog post 2',
	'content':'second post content',
	'date_posted':'may 15, 1998'

	}
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title=about)


@app.route("/register", methods=['GET', 'POST'])
def RegForm():
	form=RegForm()
	if form.validate_on_submit():
		flash('account created for','success')
		return redirect (url_for('/home'))
	return render_template('register.html', title=register , form=form)


@app.route("/Login")
def Login():
	form=Login()
	return render_template('login.html', title=Login, form=form)


if __name__ == '__main__':
    app.run(debug=True)