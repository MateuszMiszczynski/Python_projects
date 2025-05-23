from flask import Flask, render_template, jsonify, redirect, url_for,request
from sniffing import sniffer

app = Flask(__name__) # tworzymy instancje czyli obiekt flaska (niezbędne)

@app.route('/') # dekorator ktory mówi "jak uzytkownik będzie na adresie "/" to wykonaj to (adresie URL)"
def index():
    show_site = request.args.get("show_site") == "1"
    if sniffer.sniffing:
        packets_to_html = []
    else:
            packets_to_html = sniffer.get_recent_packets() # przypisuje pakiety z naszej funkcji z sniffer.py ktora czyli liste z bufforem do zmiennej "packets_to_html"
    return render_template('index.html', packets=packets_to_html,resolve_site = sniffer.resolve_site) # wyświetla nam index.html i przekazuje 
    # informacje do html-a (dokładniej do szablonu Jinja). Teraz "packets" (w html) niosą informacje z "packets_to_html"


@app.route('/start')
def start():
    sniffer.start_sniffing() # uruchamia sniffowanie, scapy zaczyna nasluchiwac pakiety
    return redirect(url_for("index")) # wyświetla index.html

@app.route('/stop')
def stop():
    sniffer.stop_sniffing() # zatrzymuje sniffowanie
    return redirect(url_for("index")) # wyświetla index.html

# @app.route('/packets') # endpoint, udostępnia dane jako JSON dla JavaScriptu w przeglądarce (nie ma jeszcze zastosowania)
# def packets():
#     data = sniffer.get_recent_packets() # # przypisuje pakiety z naszej funkcji z sniffer.py do zmiennej "data"
#     return jsonify(data) # przekształca listę pakietów do JSON do pobrania przez HTML


@app.route("/toggle-site", methods=["POST"])
def toggle_site():
    new_value = request.form.get("resolve_site") == "true"
    sniffer.set_resolve_site(new_value)
    return redirect(url_for("index"))

if __name__ == '__main__': # jeśli plik został uruchomiony bezpośrednio uruchamia serwer deweloperski 
    app.run(debug=True) # pozwala na automatyczny restart po zmianach w kodzie oraz debugger w przeglądarce