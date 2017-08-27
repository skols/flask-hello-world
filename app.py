# Flask Hello World

# import the Flask class from the flask package
from flask import Flask

# Create the application object
app = Flask(__name__)


# Use the decorator pattern to link the view function to a URL
@app.route("/")
@app.route("/hello")
# Definte the view using a function, which returns a string
def hello_world():
    return "Hello, World!"


# Start the development server using the run command
if __name__ == "__main__":
    app.run()
