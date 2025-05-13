
## 🌐 About the App

**`packet-sniffer-webapp`** is a lightweight web application for real-time network packet sniffing and visualization. It combines low-level packet capture with a user-friendly interface for displaying key information.

### 🔍 What it does:
- Captures network traffic using **Scapy**
- Identifies and displays key protocols: **DNS**, **HTTP**, **TCP**, **UDP**, **ICMP**
- Runs the sniffer in a **separate thread** to keep the Flask UI responsive
- Displays captured packets in a **web dashboard**
- Saves captured data as **JSON logs**
- Allows downloading the logs from the browser

### 🧪 Technologies used:
- **Python 3**
- **Flask** – lightweight web framework
- **Scapy** – for low-level packet sniffing and protocol parsing
- **Threading** – for background sniffing
- **Jinja2 (HTML templates)** – for rendering the dashboard
- **CSS** – for basic styling
- **JSON** – structured log output

---

## ▶️ How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/packet-sniffer-webapp.git
cd packet-sniffer-webapp
