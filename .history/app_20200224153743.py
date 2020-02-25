from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =

# Notice how you define route in python
@app.route('/')
def index():
    return render_template('index.html')


# MAIN PROGRAM START
if __name__ == "__main__":
    app.run(debug=True)
