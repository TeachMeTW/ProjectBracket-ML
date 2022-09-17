import flask


app = flask.Flask(__name__)

@app.route("/dab")
def init():
    return "bruh"


if __name__ == "__main__":
    app.run(debug=True)