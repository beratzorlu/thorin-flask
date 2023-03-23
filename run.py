import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"

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