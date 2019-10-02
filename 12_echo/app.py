from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello"

@app.route('/auth', methods = ["POST"])
def auth():
    print(app)
    print(request)
    print(request.form)
    print(request.form["Username"])
    print("info")
    print(request.headers)
    return render_template("response.html",
    username = request.form.get('Username'),
    method = request.method)

@app.route('/index.html')
def hello_world():
    print(app)
    print(request)
    print(request.form)
    return render_template("index.html")

if __name__ == "__main__":
        app.debug = True
        app.run()
