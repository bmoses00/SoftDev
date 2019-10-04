# Brian Moses
# SoftDev pd 2
# k#16: Oh yes, perhaps I do
# 10/3/19

from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
app = Flask(__name__)

@app.route('/')
def main():
    print ('-------------------------------------------')
    # print(login)
    # print("------------------------------------")
    # print(session['username'])
    # print("------------------------------------")
    # print(session['password'])
    # if (login):
    #     return render_template("welcome.html", username = request.args.get('Username'))

    # hardcoded username/pass combo
    session['username'] = 'chicken'
    session['password'] = 'portenders'
    # we use try-catch block to make sure we don't get an error if
    # session['loggedIn'] is undefined, which it would be if it's the first
    # time the page had been loaded
    try:
        if session['loggedIn']:
            return render_template("welcome.html", username = session['userUsername'])
    except:
        session['loggedIn'] = False
    return render_template("index.html",
                           username = request.args.get('Username'),
                           password = request.args.get('Password'))

@app.route('/logout')
def help():
    session['loggedIn'] = False
    return redirect(url_for('main'))

@app.route('/auth')
def authenticate():
    # checks if they entered the right username/pass combo
    if ((request.args.get('Username')) == session['username']
    and request.args.get('Password') == session['password']):
        session['userUsername'] = request.args.get('Username')
        session['loggedIn'] = True
        flash("You have logged in!")
        return render_template("welcome.html", username = request.args.get('Username'))
    else:
        return render_template("error.html" # checks if user has wrong username, pass, or both
                             , usernameWrong = request.args.get('Username') != session['username']
                             , passwordWrong = request.args.get('Password') != session['password'])
    #return redirect("http://www.xkcd.com")
    # return render_template("response.html")
    return 'Else did not trigger. Code is wrong.'

if __name__ == "__main__":
        app.secret_key = os.urandom(32)
        app.debug = True
        app.run()
