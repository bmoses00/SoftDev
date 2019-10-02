from flask import Flask, render_template, request, session
import os
app = Flask(__name__)

@app.route('/')
def main():
    session['username'] = 'portenders'
    print("------------------------------------")
    print (session['username'])
    print("------------------------------------")
    return "Hello"

if __name__ == "__main__":
        app.secret_key = os.urandom(32)
        app.debug = True
        app.run()
