# Templates
'''Flask Templates are a way of using prewritten HTML with Flask, because 
writing everyhting from scratch would be too tedious. You can utilize 
templates by creating a templates folder in the home directory and storing 
all your HTML files there, and Flask will know where to look for them. '''

from flask import Flask, render_template 
app = Flask(__name__)

'''you can also pass variables into the html, using Jinja. The Jinja formatting 
requires you to use double curly braces {{VAR}} to enclose the variables 
in the HMTL. This is great when you want pages to have the same foundation 
but still something unique or specific to each one.   '''

@app.route('/')
def index(): 
    links = ['youtube.com', 'facebook.com', 'twitter.com']
    return render_template('example.html',
    links = links, 
     var='variable passed in' #you can comment this out to see if/else in jinja HTML at work
     )

if __name__ == '__main__': 
    app.run(debug=True)