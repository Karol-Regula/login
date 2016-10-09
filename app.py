from flask import Flask, render_template, request, session, url_for, redirect
from utils import authenticate

app = Flask(__name__)
app.secret_key = "Hello!"

@app.route("/")
@app.route("/welcome/")
def welcome ():
    if (len(session.keys()) > 0):
        return render_template('welcome.html',user = session['user'])
    else:
        return redirect(url_for('login'))

@app.route("/login/")
def login ():
    return render_template('form.html')

@app.route("/authenticate/", methods = ['POST']) #only post requests allowed
def auth():
    if (request.form['action'] == "login"):
        out = authenticate.login(request.form['user'], request.form['password'])
        if (out[1] == 1):
            session['user'] = request.form['user']
            return redirect(url_for('welcome'))
        else:
            return out[0]
    elif (request.form['action'] == "register"):
        return authenticate.register(request.form['user'], request.form['password'])

@app.route("/logout/", methods = ['POST', 'GET'])
def logout():
    if (len(session.keys()) > 0):
        session.pop('user')
    return render_template('form.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
