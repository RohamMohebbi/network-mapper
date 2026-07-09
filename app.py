from flask import Flask, render_template, jsonify
import nmap

app = Flask(__name__)

def scan_network():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.1.0/24', arguments='-sn')
    
    devices = []
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            devices.append({
                'ip': host,
                'hostname': nm[host].hostname(),
                'status': 'online'
            })
    return devices

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/devices')
def get_devices():
    devices = scan_network()
    return jsonify(devices)

if __name__ == '__main__':
    app.run(debug=True)