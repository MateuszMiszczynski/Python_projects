from flask import Flask, render_template
from sniffing.sniffer import start_sniffing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-sniffing')
def start_sniffing_route():
    start_sniffing()
    return "Sniffing started!"

if __name__ == '__main__':
    app.run(debug=True)