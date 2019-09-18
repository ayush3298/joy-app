from flask import Flask, render_template, request
from database import database

app = Flask(__name__)
db = database()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/data", methods=["GET", "POST"])
def get_data():
    if request.method == "POST":
        name = request.form["name"]
        color = request.form["color"]
        cat_or_dog = request.form["dog_or_cat"]
        db.insert_data(name, color, cat_or_dog)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
