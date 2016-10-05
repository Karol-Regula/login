from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def render ():
    print request.headers #info about browser that made the request
    return render_template('form.html')

@app.route("/authenticate/", methods = ['POST']) #only post requests allowed
def auth():
    #print request.headers
    if (request.form['action'] == 'Login'):
        credentials = open('credentials.csv', 'r')
        for line in credentials:
            comma = line.find(',')
            print line[comma + 1:]
            print hashlib.sha224(request.form['password']).hexdigest()
            if (request.form['user'] == line[:comma] and hashlib.sha224(request.form['password']).hexdigest() + '\n' == line[comma + 1:]):
                return render_template('authentication.html', result = "Login successful")
            if (request.form['user'] == line[:comma] and not hashlib.sha224(request.form['password']).hexdigest() + '\n' == line[comma + 1:]):
                return render_template('form.html', message = "Incorrect password")
        return render_template('form.html', message = "Username does not exist")
    else: #registering
        credentials = open('credentials.csv', 'r')
        duplicate = False
        for line in credentials:
            comma = line.find(',')
            if (request.form['user'] == line[:comma]):
                duplicate = True
        if (duplicate):
            return render_template('form.html', message = "Username already exists")
        else:
            credentials = open('credentials.csv', 'a')
            credentials.write(request.form['user'] + ',' + hashlib.sha224(request.form['password']).hexdigest() + '\n')
            return render_template('form.html', message = "Registration Successful!")

if __name__ == '__main__':
    app.debug = True
    app.run()
