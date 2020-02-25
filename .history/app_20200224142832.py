from flask import Flask, render_template

app = Flask(__name__)

# Notice how you define route in python
@app.route('/')
def index():
    return render_template('index.html')


# MAIN PROGRAM START
if __name__ == "__main__":
    app.run(debug=True)
