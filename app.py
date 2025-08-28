from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Functions that we’ll also expose as routes
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return render_template("about.html")
