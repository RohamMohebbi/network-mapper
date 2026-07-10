# 🌐 Network Mapper Pro

## Advanced Network Topology Scanner with OS Detection & Port Scanning

A professional network mapping tool that automatically discovers devices on your network, detects operating systems, scans open ports, and visualizes everything as an interactive graph.

---

## ✨ Features

- 🔍 Auto-scan your local network
- 🖥️ Operating system detection
- 🔌 Open port scanning & service detection
- 📊 Interactive network graph visualization
- 🎯 Click any device to see detailed info
- ⚡ Fast and lightweight
- 📱 Responsive design

---

## 🛠️ Tech Stack

| Layer | Technology |
|:---|:---|
| **Backend** | Python, Flask |
| **Network Scanning** | python-nmap |
| **Graph Rendering** | Vis.js |
| **Frontend** | HTML, CSS, JavaScript |

---

## 📁 Project Structure

```
network-mapper/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Frontend page
├── static/
│   └── style.css       # Custom styling
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── network-map.png     # Screenshot preview
```

---

## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/RohamMohebbi/network-mapper.git
cd network-mapper
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```

### 4. Open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. The app scans your local network using `python-nmap` with OS detection
2. It identifies devices, operating systems, and open ports
3. Vis.js renders an interactive network graph
4. Click on any device to see full details including open ports

---

## 📸 Preview

![Network Map](network-map.png)

---

## 🔧 Requirements

- Python 3.7+
- Flask
- python-nmap
- Nmap installed on your system (download from nmap.org for Windows)

---

## 👨‍💻 Developer

**Roham Mohebbi**
- 🌐 [GitHub](https://github.com/RohamMohebbi)

---

## ⭐ Support

If you like this project, give it a star ⭐!

---

**📧 Questions or ideas? I'd love to hear them!**
