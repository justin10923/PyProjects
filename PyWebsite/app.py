from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/homepage")
def index():
    return render_template("homepage.html")

@app.route("/login")
def login():
    ...


@app.route("/hello/<user>")
def hello(user):
    return render_template("user.html", input=user)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

