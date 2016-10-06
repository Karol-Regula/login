from flask import Flask, render_template, request, session
from utils import authenticate

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def render ():
    print request.headers #info about browser that made the request
    return render_template('form.html')

@app.route("/authenticate/", methods = ['POST']) #only post requests allowed
def auth():
    print request.form['action']
    if (request.form['action'] == "login"):
        return authenticate.login(request.form['user'], request.form['password'])
    elif (request.form['action'] == "register"):
        return authenticate.register(request.form['user'], request.form['password'])

if __name__ == '__main__':
    app.debug = True
    app.run()
