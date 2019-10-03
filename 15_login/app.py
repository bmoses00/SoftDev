from flask import Flask, render_template, request, session, redirect, url_for
import os
app = Flask(__name__)
login = False

@app.route('/')
def main():
    print(login)
    session['username'] = 'chicken'
    session['password'] = 'portenders'
    print("------------------------------------")
    print(session['username'])
    print("------------------------------------")
    print(session['password'])

    # if (login):
    #     return render_template("welcome.html", username = request.args.get('Username'))

    return render_template("index.html",
                           username = request.args.get('Username'),
                           password = request.args.get('Password'))

@app.route('/auth')
def authenticate():
    if ((request.args.get('Username')) == session['username']
    and request.args.get('Password') == session['password']):
        login = True
        print(login)
        return render_template("welcome.html", username = request.args.get('Username'))
    else:
        return render_template("error.html"
                             , username = request.args.get('Username')
                             , password = request.args.get('Password'))
    #return redirect("http://www.xkcd.com")
    # return render_template("response.html")
    return 'this did not work'

if __name__ == "__main__":
        app.secret_key = os.urandom(32)
        app.debug = True
        app.run()
