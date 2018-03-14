# Flask 

## The basic anatomy of a Flask App: 
[Youtube video ](https://www.youtube.com/watch?v=zKI66AuEGkA&list=PLXmMXHVSvS-AjwTOtiW1DXFYTgUlrUmHV&index=3)
```python 

from flask import Flask 

'''boiler plate code to initialize the app, which is the 
main way we interact with our code'''
app = Flask(__name__)

'''below you will add route functuons: any time someone types in an address into their browser, the 
address is directed to the corresponding route function. Anything that 
happens in the specific route function, happens on that webpage '''

# '/' is the index route - the home 
@app.route('/')
def index(): 
    return '<h1> Hello </h1>'

'''routes can take argments. You must specify them with <> in the decorator 
and the same variable name should be an arugmeent for the function '''
@app.route('/home/<place>')
def home(place):
    return '<h1> You are on the {} page! </h1>'.format(place)

# Methods 
'''methods are acheived by specifying the type in the route decoroator. 
by default, all methods are set to "GET" requests. '''
@app.route('/method', methods = ['GET', 'POST'])
def method():
    return ''

if __name__ == '__main__': 
    app.run(debug=True)

```

---------------------------------------------------------------

## Types of Requests: 

[link](http://www.restapitutorial.com/lessons/httpmethods.html)

There are many types of requests, but you will mostly use just a few. Getting a 405 Error, Method not Allowed, means you are using the wrong request type, and solution is to double check your permessions in your route decorator and double check the funcionality you are trying to execute. 

**GET** : for retrieving information that you are not trying to change. eturns a representation in XML or JSON and an HTTP response code of 200 (OK). In an error case, it most often returns a 404 (NOT FOUND) or 400 (BAD REQUEST).

**POST** : Create new data. On successful creation, return HTTP status 201. 

**PUT** : update/replace data. Used sparingly due to its similary with POST. 

**PATCH** : udate/modify data.  The PATCH request only needs to contain the changes to the resource, not the complete resource.

**DELETE** : delete data 

---------------------------------------------------------------

## Templates 

```python 

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

```