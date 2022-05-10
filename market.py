from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html')


""" #dynamic routes
@app.route("/about/<username>")
def about_page(username):
	return f'<h1>This is the about page of {username}</h1>' """


#checks to see if run.py file has executed directly and not imported
if __name__ == "__main__":
    app.run(debug=True) 