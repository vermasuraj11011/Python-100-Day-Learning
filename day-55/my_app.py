from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user/<name>/<int:age>")
def greeting(name, age):
    age += 2
    return f"<h1>Hello {name}!</h1> <br> <p>Your age is {age}<p>"


@app.route("/cat")
def get_cat():
    return '<iframe src="https://giphy.com/embed/ryM5tbbRLHE3qNj8Is" \
            width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen>\
            </iframe><p><a href="https://giphy.com/gifs/buzzfeed-dog-puppies-funny-animals-ryM5tbbRLHE3qNj8Is"> \
            via GIPHY</a></p>>'


if __name__ == "__main__":
    app.run(debug=True)
