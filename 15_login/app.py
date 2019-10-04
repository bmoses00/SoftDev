from flask import Flask, render_template, request, session, redirect, url_for
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
    session['username'] = 'chicken'
    session['password'] = 'portenders'
    try:
        if session['loggedIn']:
            return render_template("welcome.html", username = session['userUsername'])
                                                # because they are logged in,
                                                # their username must be the
                                                # same as only valid one
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
    if ((request.args.get('Username')) == session['username']
    and request.args.get('Password') == session['password']):
        session['userUsername'] = request.args.get('Username')
        session['loggedIn'] = True
        return render_template("welcome.html", username = request.args.get('Username'))
    else:
        return render_template("error.html" # checks if user has wrong username, pass, or both
                             , usernameWrong = request.args.get('Username') != session['username']
                             , passwordWrong = request.args.get('Password') != session['password'])
    #return redirect("http://www.xkcd.com")
    # return render_template("response.html")
    return 'something went wrong'

if __name__ == "__main__":
        app.secret_key = os.urandom(32)
        app.debug = True
        app.run()
