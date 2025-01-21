from flask import Flask, send_file

app = Flask(__name__)

@app.route('/deck')
def deck():
    return send_file('deck.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)
