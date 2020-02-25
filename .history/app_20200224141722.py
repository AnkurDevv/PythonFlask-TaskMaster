from flask import Flask

app = Flask(__name__)

# Notice how you define route in python
@app.route('/')
def index():
    return "Hello, World!"


# MAIN PROGRAM START
if __name__ == "__main__":
    app.run(debug=True)
