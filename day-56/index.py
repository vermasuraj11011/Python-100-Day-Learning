from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("suraj.html")


@app.route('/identity')
def identity():
    return render_template("index.html")


@app.route('/contact')
def contact():
    return render_template("contact-me.html")


@app.route('/hobbies')
def hobbies():
    return render_template("hobbies.html")


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
