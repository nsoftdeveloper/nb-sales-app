from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'NB Sales App'

app.run(debug=True)