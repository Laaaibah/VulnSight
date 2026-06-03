from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import json
from datetime import datetime
from utils.scanner import NetworkScanner
from utils.vulnerability_processor import VulnerabilityProcessor
import platform
import socket

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Initialize scanner and processor
scanner = NetworkScanner()
processor = VulnerabilityProcessor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        target = request.form.get('target')
        scan_type = request.form.get('scan_type')
        
        if scan_type == 'quick':
            results = scanner.quick_scan(target)
        elif scan_type == 'comprehensive':
            results = scanner.comprehensive_scan(target)
        else:
            results = scanner.basic_scan(target)
        
        # Save scan results
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"scan_result_{timestamp}.json"
        with open(os.path.join('static', 'results', filename), 'w') as f:
            json.dump(results, f)
        
        # Process vulnerabilities
        processed_results = processor.process_scan_results(results)
        
        return render_template('results.html', 
                              results=processed_results, 
                              target=target,
                              scan_type=scan_type,
                              timestamp=timestamp)
    
    return render_template('scan.html')

@app.route('/history')
def history():
    results_dir = os.path.join('static', 'results')
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    scan_files = []
    for file in os.listdir(results_dir):
        if file.endswith('.json'):
            scan_files.append(file)
    
    return render_template('history.html', scan_files=scan_files)

@app.route('/view_scan/<filename>')
def view_scan(filename):
    file_path = os.path.join('static', 'results', filename)
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            results = json.load(f)
        
        processed_results = processor.process_scan_results(results)
        
        return render_template('results.html', 
                              results=processed_results, 
                              target=results.get('target', 'Unknown'),
                              scan_type=results.get('scan_type', 'Unknown'),
                              timestamp=filename.split('_')[2].split('.')[0])
    
    return redirect(url_for('history'))

# ✅ NEW: API route to provide system information
@app.route('/api/system_info')
def system_info():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        os_name = platform.system()
        os_version = platform.version()
        architecture = platform.machine()
        
        return jsonify({
            'hostname': hostname,
            'ip': ip_address,
            'os': os_name,
            'os_version': os_version,
            'architecture': architecture
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('static/results', exist_ok=True)
    app.run(debug=True)
