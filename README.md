# 🐍 Python Projects Repository

Welcome to my collection of Python projects! This repository gathers various apps and scripts built to explore programming concepts, sharpen my Python skills, and showcase my progress. Projects range from GUI-based apps to digital signal processing experiments.

---


### 🌐 `packet-sniffer-webapp`
A web-based network packet sniffer built using **Flask** and **Scapy**. It allows you to monitor, classify, and log live network traffic through a clean web interface.

**Key Features:**
- ✅ Real-time packet capturing via Scapy
- 🔍 Protocol detection: DNS, HTTP, TCP, UDP, ICMP
- 🧵 Runs sniffing in a background thread (non-blocking Flask UI)
- 📝 Logs traffic data to JSON (timestamp, IPs, protocol, length)
- 🌐 Web dashboard with live updates and packet table
- 📥 Log file download support

**Tech Highlights:**
- Python threading for asynchronous packet capture
- Flask for frontend rendering (Jinja2 templates + static CSS)
- JSON log format for structured data and further analysis

This project showcases the integration of low-level network analysis with modern web development.

---


### 📈 `DSP-scripts`
A folder with Python code from **Digital Signal Processing** labs. It includes implementations of core DSP concepts and visualizations.

**What’s inside:**
- ⚙️ Discrete and Fast Fourier Transforms (DFT & FFT)
- 🪟 Windowing techniques (Hamming, Blackman, Chebyshev, etc.)
- 🔍 Frequency spectrum analysis
- ➕ Zero-padding and resolution enhancement

Perfect for combining theory with practice using Python’s scientific stack.

---
## 📂 Projects Included

### 📊 `tkinter-csv-app`
A desktop application with a graphical interface built using **Tkinter**, designed for working with CSV files.

**Key Features:**
- ✅ Generate random CSV datasets (custom number of rows)
- 🔍 Search and filter by keywords or female names
- 🔃 Sort data externally by column (e.g., Name, Price, etc.)
- 📁 Simple file dialog integration

This project demonstrates GUI design, file handling, data generation, and external sorting techniques.

---


## Requirements

- Python 3.x
- **For `packet-sniffer-webapp`:**
  - `Flask`, `Scapy`, `json`, `threading`
- **For `dsp-labs`** (some scripts):  
  - `numpy`, `matplotlib` (for signal analysis and plotting)
- **For `tkinter-csv-app`**:  
  - Built-in: `tkinter`, `csv`, `os`, `random`, `heapq`, `pathlib`

