
## About the App

**`packet-sniffer-webapp`** is a lightweight web application for real-time network packet sniffing and visualization. It combines low-level packet capture with a user-friendly interface for displaying key information.

### What it does:
- Captures network traffic using **Scapy**
- Identifies and displays key protocols: **DNS**, **HTTP**, **TCP**, **UDP**, **ICMP**
- Runs the sniffer in a **separate thread** to keep the Flask UI responsive
- Displays captured packets in a **web dashboard**
- Saves captured data as **JSON logs**
- Allows downloading the logs from the browser

### Technologies used:
- **Python 3**
- **Flask** – lightweight web framework
- **Scapy** – for low-level packet sniffing and protocol parsing
- **Threading** – for background sniffing
- **Jinja2 (HTML templates)** – for rendering the dashboard
- **CSS** – for basic styling
- **JSON** – structured log output

---


**Summary:**
- `app.py`  
  Launches the Flask server, renders the interface, and connects to the sniffing logic.
  
- `sniffer.py`  
  Contains all functions for capturing and parsing network packets (DNS, HTTP, TCP, etc.). It logs the captured data as JSON.

- `index.html`  
  The user interface where you can start/stop capturing and download logs. It uses Jinja2 templating.

- `styles.css`  
  Defines the appearance of the dashboard (layout, buttons, fonts, etc.).

- `logs/`  
  Stores log files created during each capture session in JSON format.

- `requirements.txt`  
  Lists Python packages required to run the application.


---



##  How to Run

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/packet-sniffer-webapp.git
cd packet-sniffer-webapp

# 2. Create and activate a virtual environment (recommended)

# On Linux / macOS / Git Bash:
cd <path_to_packet-sniffer-webapp>
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app with administrator/root privileges
# Packet sniffing uses raw sockets, which require elevated privileges.

# On Linux/macOS:
sudo python app.py

# On Windows (run terminal as Administrator):
python app.py

# 5. Open your browser and go to:
http://127.0.0.1:5000/

# Use the Start/Stop buttons to control the capture and download logs.

