from flask import Flask, render_template, jsonify, redirect, url_for
from sniffing import sniffer

app = Flask(__name__)

@app.route('/')
def index():
    packets = sniffer.get_recent_packets() 
    return render_template('index.html', packets=packets)


@app.route('/start')
def start():
    sniffer.start_sniffing()
    return redirect(url_for("index"))

@app.route('/stop')
def stop():
    sniffer.stop_sniffing()
    return redirect(url_for("index"))
@app.route('/packets')
def packets():
    data = sniffer.get_recent_packets()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)