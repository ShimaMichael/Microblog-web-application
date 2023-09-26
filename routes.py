from app import app
from  flask import render_template as rt

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Shami'} 
	posts = [
		{
			'author': {'username': 'Daddy:'},
			'body':'Beautiful day in London'
		},
		{
			'author': {'username': 'Snickerdoodle:'},
			'body': 'you are so sweet'
		}
	]
	return  rt('index.html', title='Home', user=user, posts=posts)
