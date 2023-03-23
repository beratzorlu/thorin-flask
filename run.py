import os
from flask import Flask, render_template

app = Flask(__name__)

# Flask expects called html files to be in a file named templates.
# The folder should be on the same level as the run.py file.
# The @app.route("/") decorator allows the route and the index()
# to be called together, one won't be called without the other.


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# __main__ is the name of the default module of Python. We run this first,
# it will be run directly.
# NEVER have debug=True in production deployments or while submitting
# assignments.
# Otherwise it will allow arbitrary code to be run.
# Change it to false when you're finished with development.


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)