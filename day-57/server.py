import random
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1, 10)
    cur_year = datetime.now().year
    return render_template("index.html", rand_num=random_num, cur_year=cur_year)


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
