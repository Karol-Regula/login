from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def render ():
    print request.headers #info about browser that made the request
    return render_template('form.html')

@app.route("/authenticate/", methods = ['POST']) #only post requests allowed
def auth():
    print request.headers
    if (request.form['user'] == "bill" and request.form['password'] == "drowssap"):
        return render_template('positive.html')
    else:
        return render_template('negative.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
