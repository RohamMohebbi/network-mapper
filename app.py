from flask import Flask, render_template, jsonify
import nmap
import socket
import re
import time
from collections import defaultdict

app = Flask(__name__)

def get_network_info():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    subnet = '.'.join(local_ip.split('.')[:-1]) + '.0/24'
    return subnet

def scan_network():
    nm = nmap.PortScanner()
    subnet = get_network_info()
    
    # aggressive but quick scan
    nm.scan(hosts=subnet, arguments='-O -sV -T4 -F --version-light')
    
    devices = []
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            device = {
                'ip': host,
                'hostname': nm[host].hostname() or 'Unknown',
                'status': 'online',
                'os': 'Unknown',
                'ports': [],
                'mac': 'N/A',
                'vendor': 'Unknown'
            }
            
            if 'osmatch' in nm[host] and nm[host]['osmatch']:
                device['os'] = nm[host]['osmatch'][0]['name'][:30]
            
            if 'addresses' in nm[host]:
                if 'mac' in nm[host]['addresses']:
                    device['mac'] = nm[host]['addresses']['mac']
                if 'ipv4' in nm[host]['addresses']:
                    device['ip'] = nm[host]['addresses']['ipv4']
            
            # vendor lookup from mac
            if device['mac'] != 'N/A':
                vendor_file = '/usr/share/nmap/nmap-mac-prefixes'
                try:
                    with open(vendor_file, 'r') as f:
                        for line in f:
                            if device['mac'][:8].upper() in line:
                                device['vendor'] = line.split()[1]
                                break
                except:
                    pass
            
            if 'tcp' in nm[host]:
                for port, info in nm[host]['tcp'].items():
                    if info['state'] == 'open':
                        device['ports'].append({
                            'port': port,
                            'service': info['name'],
                            'version': info.get('version', 'N/A')
                        })
            
            devices.append(device)
    
    return sorted(devices, key=lambda x: x['ip'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/devices')
def get_devices():
    try:
        start = time.time()
        devices = scan_network()
        duration = round(time.time() - start, 2)
        return jsonify({
            'success': True,
            'devices': devices,
            'count': len(devices),
            'scan_time': duration
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
