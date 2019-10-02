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
                           username = request.form.get('Username'),
                           password = request.form.get('Password'))

@app.route('/auth')
def authenticate():
    # print (request.form.get('Username'))
    print(request.form.get('Username'))
    #return redirect("http://www.xkcd.com")
    return render_template("response.html")

if __name__ == "__main__":
        app.secret_key = os.urandom(32)
        app.debug = True
        app.run()
