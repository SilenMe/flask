from flask import Flask, render_template

app=Flask(__name__)

all_posts=[
{
	'title':'Post 1',
	'content':'Post 1 content',
	'author':'Sahani'
},
{
	'title':'Post 2',
	'content':'Post 2 content'
}]

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/posts')
def posts():
	return render_template('posts.html',posts=all_posts) # now we can use this Post variable in templates or wherever we want
 
@app.route('/home/<string:name>')#base url(just domain)

def hello(name):
	return "Hello " + name

if __name__ == '__main__':
	app.run(debug=True)
