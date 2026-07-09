# 🌐 Network Mapper

## 📡 Automated Network Topology Mapper

A Python tool that automatically scans your local network, discovers connected devices, and visualizes them as an interactive graph.

---

## ✨ Features

- 🔍 Auto-scan network and discover active devices
- 📊 Graphical visualization of devices as nodes connected to the router
- 🖱️ Interactive graph with zoom, drag, and hover details
- ⚡ Fast and lightweight
- 🎨 Clean and simple UI

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
├── app.py              # (Main backend code)
├── templates/
│   └── index.html      # (Frontend page)
├── requirements.txt    # (Dependencies)
└── README.md           # (Project documentation)
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

1. The app scans your local network using `python-nmap`
2. It detects active devices and collects their info (IP, hostname)
3. Vis.js renders an interactive network graph
4. Each device appears as a node connected to the router

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
