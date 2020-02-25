from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.integer, primary_key=True)

# Notice how you define route in python
@app.route('/')
def index():
    return render_template('index.html')


# MAIN PROGRAM START
if __name__ == "__main__":
    app.run(debug=True)
