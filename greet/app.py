from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Return simple "Welcome" Greeting."""
    return "welcome"
@app.route('welcome/home')
def say_welcome_home():
    """Return simple "welcome home" Greeting."""
    return "welcome home"
@app.route('welcome/back')
def say_welcome_back():
    """Return simple "welcome back" Greeting."""
    return "welcome back"