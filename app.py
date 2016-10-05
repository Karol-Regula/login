from flask import Flask, render_template, request
from utils import authenticate

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def render ():
    print request.headers #info about browser that made the request
    return render_template('form.html')

@app.route("/authenticate/", methods = ['POST']) #only post requests allowed
def auth():
    return authenticate.auth(request.form['user'], request.form['password'], request.form['action'])

if __name__ == '__main__':
    app.debug = True
    app.run()
