# Intro to Flask 
# https://www.youtube.com/watch?v=zKI66AuEGkA&list=PLXmMXHVSvS-AjwTOtiW1DXFYTgUlrUmHV&index=3

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