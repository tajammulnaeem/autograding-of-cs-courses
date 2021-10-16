from flask import *

app = Flask(__name__)


@app.route("/")
def homepage():
    return "Home Page Here"

if __name__ == "__main__":
    app.run(debug=True)