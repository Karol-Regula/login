from flask import render_template
import hashlib

def login(user, password):
    credentials = open('data/credentials.csv', 'r')
    for line in credentials:
        comma = line.find(',')
        #print line[comma + 1:]
        #print hashlib.sha224(password).hexdigest()
        if (user == line[:comma] and hashlib.sha224(password).hexdigest() + '\n' == line[comma + 1:]):
            return ("Placeholder message.", 1)
        if (user == line[:comma] and not hashlib.sha224(password).hexdigest() + '\n' == line[comma + 1:]):
            return (render_template('form.html', message = "Incorrect password"), 0)
    return (render_template('form.html', message = "Username does not exist"), 0)

def register(user, password):
    credentials = open('data/credentials.csv', 'r')
    duplicate = False
    for line in credentials:
        comma = line.find(',')
        if (user == line[:comma]):
            duplicate = True
    if (duplicate):
        return render_template('form.html', message = "Username already exists")
    else:
        credentials = open('data/credentials.csv', 'a')
        credentials.write(user + ',' + hashlib.sha224(password).hexdigest() + '\n')
        return render_template('form.html', message = "Registration Successful!")
