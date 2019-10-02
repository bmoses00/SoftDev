from flask import Flask, render_template, request, session, redirect, url_for
import os
app = Flask(__name__)

@app.route('/')
def main():
    session['username'] = 'portenders'
    session['password'] = 'chicken'
    print("------------------------------------")
    print(session['username'])
    print("------------------------------------")
    print(session['password'])
    return render_template("index.html",
                           username = request.args.get('Username'),
                           password = request.args.get('Password'))

@app.route('/auth')
def authenticate():
    print(request.args.get('Username'))
    print(session['username'])
    if (request.args.get('Username')) == session['username']:
        return "nice"
    else:
        return "not nice"
    #return redirect("http://www.xkcd.com")
    # return render_template("response.html")
    return 'what'

if __name__ == "__main__":
        app.secret_key = os.urandom(32)
        app.debug = True
        app.run()
