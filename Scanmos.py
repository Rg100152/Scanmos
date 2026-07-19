# ============================================================
# SCANMOS - High-Speed Network Scanner
# Educational CLI Simulator
# Version: 1.0
# Author: Raj Gautam
# License: MIT
# Platform: PyDroid / QPython / Termux / Any Python 3.x
# ============================================================

import sys
import time
import random
import json
import os
from datetime import datetime
import platform

# ============================================================
# ANSI COLOR CODES (Cross-Platform)
# ============================================================

class Colors:
    """Terminal colors using ANSI escape codes - works everywhere"""
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    CLEAR = '\033[2J'
    HOME = '\033[H'
    HIDE_CURSOR = '\033[?25l'
    SHOW_CURSOR = '\033[?25h'

# ============================================================
# ANIMATION ENGINE (Pure Python)
# ============================================================

class Animation:
    """All animations using standard Python - no external libs"""

    @staticmethod
    def clear():
        """Clear screen"""
        sys.stdout.write(Colors.CLEAR + Colors.HOME)
        sys.stdout.flush()

    @staticmethod
    def typewrite(text, delay=0.03, color=Colors.GREEN):
        """Typewriter effect"""
        for ch in text:
            sys.stdout.write(f"{color}{ch}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(delay)
        print()

    @staticmethod
    def loading_bar(duration=2, width=40, label="Loading"):
        """Custom loading bar"""
        sys.stdout.write(Colors.HIDE_CURSOR)
        for i in range(width + 1):
            percent = int((i / width) * 100)
            filled = '█' * i
            empty = '░' * (width - i)
            sys.stdout.write(
                f"\r{Colors.CYAN}[{filled}{empty}]{Colors.RESET} "
                f"{Colors.YELLOW}{percent}%{Colors.RESET} "
                f"{Colors.DIM}{label}{Colors.RESET}"
            )
            sys.stdout.flush()
            time.sleep(duration / width)
        print(f" {Colors.GREEN}✓{Colors.RESET}")
        sys.stdout.write(Colors.SHOW_CURSOR)

    @staticmethod
    def spinner(duration=2, label="Processing"):
        """Spinner animation"""
        chars = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
        sys.stdout.write(Colors.HIDE_CURSOR)
        for _ in range(int(duration * 10)):
            for ch in chars:
                sys.stdout.write(f"\r{Colors.CYAN}{ch}{Colors.RESET} {Colors.DIM}{label}{Colors.RESET}")
                sys.stdout.flush()
                time.sleep(0.05)
        sys.stdout.write(f"\r{Colors.GREEN}✓ Done!{Colors.RESET}     \n")
        sys.stdout.write(Colors.SHOW_CURSOR)

    @staticmethod
    def pulse(text, repeats=3):
        """Pulsing text effect"""
        for _ in range(repeats):
            sys.stdout.write(f"\r{Colors.MAGENTA}{text}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.15)
            sys.stdout.write(f"\r{Colors.CYAN}{text}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.15)
        print()

    @staticmethod
    def header_border(char='═', length=60):
        """Draw header border"""
        print(f"{Colors.MAGENTA}{char * length}{Colors.RESET}")

# ============================================================
# ASCII LOGO GENERATOR (Built-in)
# ============================================================

class Logo:
    """Professional ASCII logos for ScanMos"""

    @staticmethod
    def show_startup():
        """Display animated startup logo"""
        Animation.clear()

        logo = f"""
{Colors.RED}   ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ███╗ ██████╗ ███████╗
{Colors.RED}   ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗ ████║██╔═══██╗██╔════╝
{Colors.RED}   ███████╗██║     ███████║██╔██╗ ██║██╔████╔██║██║   ██║███████╗
{Colors.RED}   ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╔╝██║██║   ██║╚════██║
{Colors.RED}   ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚═╝ ██║╚██████╔╝███████║
{Colors.RED}   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝{Colors.RESET}

{Colors.CYAN}   ╔═══════════════════════════════════════════════════════════╗
{Colors.CYAN}   ║{Colors.GREEN}     HIGH-SPEED NETWORK SCANNER v1.0                 {Colors.CYAN}║
{Colors.CYAN}   ║{Colors.YELLOW}     Educational Simulator | Author: Raj Gautam     {Colors.CYAN}║
{Colors.CYAN}   ║{Colors.RED}     ⚠️  SIMULATED SCANS - NO REAL HACKING  ⚠️       {Colors.CYAN}║
{Colors.CYAN}   ╚═══════════════════════════════════════════════════════════╝{Colors.RESET}
"""
        for line in logo.split('\n'):
            print(line)
            time.sleep(0.02)

        Animation.header_border('─')

        # Loading sequence
        print(f"{Colors.CYAN}>> {Colors.GREEN}Initializing ScanMos Modules...{Colors.RESET}")
        time.sleep(0.3)

        modules = [
            ("Scan Engine", "✓"),
            ("Database", "✓"),
            ("Signature Database", "✓"),
            ("Network Interface", "✓"),
            ("Report Generator", "✓"),
        ]

        for name, status in modules:
            sys.stdout.write(f"   {Colors.DIM}Loading {name}...{Colors.RESET}")
            sys.stdout.flush()
            Animation.spinner(0.5, "")
            sys.stdout.write(f"\r   {Colors.GREEN}✓ {name} Loaded{Colors.RESET}     \n")
            time.sleep(0.1)

        Animation.header_border('─')
        Animation.pulse(f"{Colors.GREEN}>> SYSTEM READY <<{Colors.RESET}", 2)
        print()

    @staticmethod
    def mini_logo():
        """Small logo for dashboard"""
        logo = f"""
{Colors.RED} ███████╗ █████╗ ███╗   ██╗███╗   ███╗ ██████╗ ███████╗
{Colors.RED} ██╔════╝██╔══██╗████╗  ██║████╗ ████║██╔═══██╗██╔════╝
{Colors.RED} ███████╗███████║██╔██╗ ██║██╔████╔██║██║   ██║███████╗
{Colors.RED} ╚════██║██╔══██║██║╚██╗██║██║╚██╔╝██║██║   ██║╚════██║
{Colors.RED} ███████║██║  ██║██║ ╚████║██║ ╚═╝ ██║╚██████╔╝███████║
{Colors.RED} ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝{Colors.RESET}
"""
        print(logo)

# ============================================================
# FAKE DATA GENERATORS
# ============================================================

class FakeData:
    """Generate realistic-looking fake scan data"""

    @staticmethod
    def random_ip():
        return f"192.168.{random.randint(1,254)}.{random.randint(1,254)}"

    @staticmethod
    def random_mac():
        return ":".join(f"{random.randint(0,255):02x}" for _ in range(6))

    @staticmethod
    def random_vendor():
        vendors = [
            "Dell Inc.", "Hewlett-Packard", "Cisco Systems", "Intel Corp.",
            "VMware Inc.", "Apple Inc.", "Samsung Electronics", "Microsoft Corp.",
            "Realtek Semiconductor", "Broadcom Inc.", "Qualcomm", "ASUS",
            "Acer Inc.", "Lenovo Group", "Huawei Technologies", "Netgear",
            "TP-Link Technologies", "D-Link Systems", "Belkin", "Buffalo Tech"
        ]
        return random.choice(vendors)

    @staticmethod
    def random_os():
        oss = [
            "Ubuntu 24.04 LTS", "Debian 12.7", "CentOS Stream 9",
            "Fedora Workstation 40", "Red Hat Enterprise Linux 9",
            "Windows Server 2022", "Windows 11 Pro 24H2",
            "Windows 10 Pro 22H2", "macOS 15 Sequoia",
            "Arch Linux Rolling", "OpenBSD 7.5", "FreeBSD 14.1",
            "Alpine Linux 3.20", "Android 14 (LineageOS)",
            "Kali Linux 2024.3", "Parrot OS 6.2"
        ]
        return random.choice(oss)

    @staticmethod
    def random_ports():
        port_services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
            53: "DNS", 80: "HTTP", 110: "POP3", 111: "RPC",
            123: "NTP", 135: "MSRPC", 137: "NetBIOS", 139: "NetBIOS",
            143: "IMAP", 443: "HTTPS", 445: "SMB", 465: "SMTPS",
            587: "SMTP", 631: "IPP", 636: "LDAPS", 873: "RSYNC",
            993: "IMAPS", 995: "POP3S", 1080: "SOCKS", 1433: "MSSQL",
            1521: "Oracle", 2049: "NFS", 2082: "cPanel", 2083: "cPanelSSL",
            2086: "WHM", 2087: "WHMSSL", 2222: "SSH", 2375: "Docker",
            2376: "DockerSSL", 2480: "OrientDB", 2481: "OrientDBSSL",
            3000: "Node.js", 3306: "MySQL", 3389: "RDP", 4000: "ERLANG",
            4040: "Spark", 4145: "RPC", 4242: "LDAP", 4443: "AJP",
            4505: "Salt", 4506: "Salt", 5000: "Flask", 5001: "Webmin",
            5002: "FTP", 5003: "FTP", 5006: "TCP", 5007: "TCP",
            5432: "PostgreSQL", 5672: "AMQP", 5900: "VNC", 5901: "VNC",
            5984: "CouchDB", 5985: "WinRM", 5986: "WinRMSSL",
            6379: "Redis", 6443: "Kubernetes", 6666: "IRC", 7070: "RTSP",
            7474: "Neo4j", 7475: "Neo4jSSL", 7547: "CWMP", 8000: "HTTP",
            8008: "HTTP", 8009: "AJP", 8080: "HTTP-Proxy", 8081: "HTTP",
            8086: "InfluxDB", 8087: "HTTP", 8088: "HTTP", 8089: "HTTP",
            8090: "HTTP", 8091: "Couchbase", 8092: "Couchbase",
            8093: "Couchbase", 8094: "Couchbase", 8095: "HTTP",
            8140: "Puppet", 8181: "HTTP", 8222: "VMware", 8243: "HTTPS",
            8333: "Bitcoin", 8384: "Syncthing", 8443: "HTTPS",
            8686: "DynamoDB", 8765: "HTTP", 8888: "HTTP", 9000: "Portainer",
            9001: "HTTP", 9042: "Cassandra", 9090: "Prometheus",
            9092: "HTTP", 9093: "HTTP", 9200: "Elasticsearch",
            9300: "Elasticsearch", 9418: "Git", 9443: "HTTPS",
            9999: "HTTP", 10000: "Webmin", 10001: "HTTP",
            11211: "Memcached", 11212: "Memcached", 11213: "Memcached",
            11214: "Memcached", 27017: "MongoDB", 27018: "MongoDB",
            27019: "MongoDB", 28017: "MongoDB", 31337: "Elite"
        }
        # Select 4-8 random ports
        selected_ports = random.sample(list(port_services.keys()), random.randint(4, 8))
        return {port: port_services[port] for port in sorted(selected_ports)}

    @staticmethod
    def random_banner(port, service):
        banners = {
            "SSH": ["OpenSSH_9.8p1", "OpenSSH_9.2p1", "OpenSSH_8.9p1", "Dropbear SSH 2024.1"],
            "HTTP": ["Apache/2.4.59", "nginx/1.27.1", "lighttpd/1.4.76", "Caddy/2.8.4"],
            "HTTPS": ["Apache/2.4.59 (SSL)", "nginx/1.27.1 (TLS)", "Caddy/2.8.4 (TLS)"],
            "MySQL": ["MySQL 8.0.39", "MariaDB 11.5.2", "Percona Server 8.4.0"],
            "FTP": ["vsftpd 3.0.5", "ProFTPD 1.3.8b", "FileZilla Server 1.8.2"],
            "SMTP": ["Postfix 3.9.0", "Exim 4.98", "Sendmail 8.18.0"],
            "DNS": ["BIND 9.18.28", "PowerDNS 4.9.3", "Unbound 1.21.0"],
            "Redis": ["Redis 7.4.0", "Redis 7.2.6"],
            "MongoDB": ["MongoDB 7.0.15", "MongoDB 6.0.17"],
            "MSSQL": ["Microsoft SQL Server 2022 SP2", "Azure SQL Edge 1.0"],
            "PostgreSQL": ["PostgreSQL 16.4", "PostgreSQL 15.8"],
            "RDP": ["Microsoft RDP 10.0", "xrdp 0.9.24", "Remote Desktop Protocol"],
            "VNC": ["TightVNC 1.3.10", "RealVNC 7.11", "TigerVNC 1.14.1"],
            "SMTP": ["Postfix 3.9.0", "Exim 4.98", "Sendmail 8.18.0"],
            "Telnet": ["Microsoft Telnet Server", "OpenBSD Telnetd", "Linux telnetd"],
            "NetBIOS": ["Samba 4.21.0", "Windows NetBIOS"],
            "SMB": ["SMBv3 11.0", "SMBv2 6.2", "Samba 4.21.0"],
            "SOCKS": ["Tor SOCKS5", "Dante SOCKS", "SSH SOCKS"],
            "Docker": ["Docker Engine 27.1", "Docker 26.1"],
            "Node.js": ["Node.js 20.17.0", "Node.js 18.20.4"],
            "Flask": ["Flask 3.0.3", "Flask 2.3.3"],
            "Webmin": ["Webmin 2.111", "Webmin 2.105"],
            "VNC": ["TightVNC 1.3.10", "RealVNC 7.11", "TigerVNC 1.14.1"],
            "RDP": ["Microsoft RDP 10.0", "xrdp 0.9.24", "Remote Desktop Protocol"],
            "AMQP": ["RabbitMQ 4.0.2", "ActiveMQ 6.1.2"],
            "CouchDB": ["CouchDB 3.4.1", "CouchDB 3.3.3"],
            "Kubernetes": ["Kubernetes v1.30.4", "K3s v1.29.6"],
            "Prometheus": ["Prometheus 2.55.0", "Prometheus 2.53.0"],
            "Elasticsearch": ["Elasticsearch 8.15.0", "Elasticsearch 8.14.0"],
            "Memcached": ["Memcached 1.6.29", "Memcached 1.6.28"],
            "MongoDB": ["MongoDB 7.0.15", "MongoDB 6.0.17"],
            "Cassandra": ["Cassandra 5.0.2", "Cassandra 4.1.6"],
            "Git": ["Git server", "GitLab", "Gitea"],
            "Elite": ["Elite Port", "Backdoor", "Unknown Service"]
        }
        return random.choice(banners.get(service, [f"{service}/1.0"]))

    @staticmethod
    def random_security_score():
        """Return security rating and score"""
        scores = [
            {"rating": "🟢 LOW RISK", "score": random.randint(70, 95)},
            {"rating": "🟡 MEDIUM RISK", "score": random.randint(40, 69)},
            {"rating": "🔴 HIGH RISK", "score": random.randint(10, 39)}
        ]
        weights = [0.35, 0.40, 0.25]  # Lower risk more likely
        return random.choices(scores, weights=weights)[0]

    @staticmethod
    def random_latency():
        return round(random.uniform(0.3, 35.0), 2)

    @staticmethod
    def random_ttl():
        return random.choice([32, 64, 128, 255])

    @staticmethod
    def random_uptime():
        return f"{random.randint(1,365)} days, {random.randint(1,23)} hours"

    @staticmethod
    def random_traffic():
        return f"{random.randint(10, 500)} MB"

# ============================================================
# SCAN ENGINE (Simulated)
# ============================================================

class ScanEngine:
    """Main scan engine - all simulated"""

    def __init__(self):
        self.history = []
        self.last_result = None
        self.scan_count = 0

    def run_scan(self, target, scan_type):
        """Execute a simulated scan"""
        self.scan_count += 1

        # Show scan header
        Animation.header_border('═')
        print(f"{Colors.CYAN}⚡ Initiating {Colors.YELLOW}{scan_type}{Colors.CYAN} on {Colors.GREEN}{target}{Colors.RESET}")
        Animation.header_border('─')

        # Scan phases with progress
        phases = [
            ("Host Discovery", "Checking if host is alive..."),
            ("Port Scanning", f"Scanning ports (1-65535)..."),
            ("Service Detection", "Identifying services on open ports..."),
            ("OS Fingerprinting", "Identifying operating system..."),
            ("Banner Grabbing", "Grabbing service banners..."),
            ("Vulnerability Check", "Checking for common vulnerabilities..."),
            ("Security Assessment", "Calculating security score...")
        ]

        for phase_name, phase_desc in phases:
            sys.stdout.write(f"{Colors.CYAN}▶ {phase_name}:{Colors.RESET} {Colors.DIM}{phase_desc}{Colors.RESET}")
            sys.stdout.flush()
            # Random progress for realism
            time.sleep(random.uniform(0.4, 1.2))
            sys.stdout.write(f"\r{Colors.GREEN}▶ ✓ {phase_name} Complete{Colors.RESET}     \n")
            sys.stdout.flush()

        # Generate fake results
        ip = target if target else FakeData.random_ip()

        ports = FakeData.random_ports()
        banners = {}
        for port, service in ports.items():
            banners[port] = FakeData.random_banner(port, service)

        security = FakeData.random_security_score()

        result = {
            "target": ip,
            "scan_type": scan_type,
            "scan_id": f"SCAN-{self.scan_count:04d}",
            "timestamp": datetime.now().isoformat(),
            "status": "Alive",
            "latency": FakeData.random_latency(),
            "ttl": FakeData.random_ttl(),
            "mac": FakeData.random_mac(),
            "vendor": FakeData.random_vendor(),
            "os": FakeData.random_os(),
            "uptime": FakeData.random_uptime(),
            "traffic": FakeData.random_traffic(),
            "ports": ports,
            "banners": banners,
            "open_ports": len(ports),
            "security_rating": security["rating"],
            "security_score": security["score"],
            "scan_duration": round(random.uniform(1.5, 4.5), 2)
        }

        self.last_result = result
        self.history.append(result)

        # Show results summary
        Animation.header_border('═')
        print(f"{Colors.GREEN}✅ SCAN COMPLETE!{Colors.RESET}")
        print(f"{Colors.DIM}Duration: {result['scan_duration']} seconds{Colors.RESET}")
        Animation.header_border('─')

        return result

# ============================================================
# REPORT GENERATOR
# ============================================================

class ReportGenerator:
    """Generate reports in various formats"""

    @staticmethod
    def export_json(data, filename=None):
        """Export as JSON"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scan_report_{timestamp}.json"

        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True, filename
        except Exception as e:
            return False, str(e)

    @staticmethod
    def export_txt(data, filename=None):
        """Export as TXT"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scan_report_{timestamp}.txt"

        try:
            with open(filename, 'w') as f:
                f.write("="*60 + "\n")
                f.write("SCANMOS SCAN REPORT\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*60 + "\n\n")

                # Basic info
                f.write("HOST INFORMATION\n")
                f.write("-"*30 + "\n")
                for key in ["target", "status", "latency", "ttl", "mac", "vendor", "os"]:
                    if key in data:
                        f.write(f"{key.upper()}: {data[key]}\n")

                f.write(f"\nUPTIME: {data.get('uptime', 'N/A')}\n")
                f.write(f"TRAFFIC: {data.get('traffic', 'N/A')}\n")
                f.write(f"OPEN PORTS: {data.get('open_ports', 0)}\n\n")

                # Security
                f.write("SECURITY ASSESSMENT\n")
                f.write("-"*30 + "\n")
                f.write(f"Rating: {data.get('security_rating', 'N/A')}\n")
                f.write(f"Score: {data.get('security_score', 0)}/100\n\n")

                # Ports
                f.write("OPEN PORTS & SERVICES\n")
                f.write("-"*30 + "\n")
                for port, service in sorted(data.get("ports", {}).items()):
                    banner = data.get("banners", {}).get(port, "N/A")
                    f.write(f"{port}/tcp - {service} - {banner}\n")

                f.write("\n" + "="*60 + "\n")
                f.write("End of Report\n")

            return True, filename
        except Exception as e:
            return False, str(e)

    @staticmethod
    def export_html(data, filename=None):
        """Export as HTML"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scan_report_{timestamp}.html"

        try:
            html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ScanMos - Scan Report</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Courier New', monospace;
            background: #0a0a0a;
            color: #c9d1d9;
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{ max-width: 900px; margin: 0 auto; background: #0d1117; padding: 30px; border-radius: 10px; border: 1px solid #30363d; }}
        h1 {{ color: #58a6ff; border-bottom: 2px solid #30363d; padding-bottom: 10px; }}
        h2 {{ color: #f0883e; margin-top: 20px; border-bottom: 1px solid #30363d; padding-bottom: 8px; }}
        .label {{ color: #8b949e; font-weight: bold; }}
        .value {{ color: #f0f6fc; }}
        .green {{ color: #3fb950; }}
        .yellow {{ color: #d29922; }}
        .red {{ color: #f85149; }}
        .port-table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
        .port-table th {{ background: #161b22; text-align: left; padding: 8px; border: 1px solid #30363d; }}
        .port-table td {{ padding: 8px; border: 1px solid #30363d; }}
        .info-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 10px 0; }}
        .info-item {{ background: #161b22; padding: 8px 12px; border-radius: 5px; }}
        .footer {{ margin-top: 30px; text-align: center; color: #484f58; font-size: 12px; border-top: 1px solid #30363d; padding-top: 15px; }}
    </style>
</head>
<body>
<div class="container">
    <h1>🔍 ScanMos - Scan Report</h1>
    <p style="color: #484f58; margin-bottom: 15px;">Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

    <h2>📡 Host Information</h2>
    <div class="info-grid">
        <div class="info-item"><span class="label">Target:</span> <span class="value">{data.get('target', 'N/A')}</span></div>
        <div class="info-item"><span class="label">Status:</span> <span class="green">{data.get('status', 'N/A')}</span></div>
        <div class="info-item"><span class="label">Latency:</span> <span class="value">{data.get('latency', 'N/A')} ms</span></div>
        <div class="info-item"><span class="label">TTL:</span> <span class="value">{data.get('ttl', 'N/A')}</span></div>
        <div class="info-item"><span class="label">MAC:</span> <span class="value">{data.get('mac', 'N/A')}</span></div>
        <div class="info-item"><span class="label">Vendor:</span> <span class="value">{data.get('vendor', 'N/A')}</span></div>
        <div class="info-item"><span class="label">OS:</span> <span class="value">{data.get('os', 'N/A')}</span></div>
        <div class="info-item"><span class="label">Uptime:</span> <span class="value">{data.get('uptime', 'N/A')}</span></div>
    </div>

    <h2>🔐 Security Assessment</h2>
    <div class="info-grid">
        <div class="info-item"><span class="label">Rating:</span> <span>{data.get('security_rating', 'N/A')}</span></div>
        <div class="info-item"><span class="label">Score:</span> <span>{data.get('security_score', 0)}/100</span></div>
    </div>

    <h2>🔌 Open Ports & Services ({data.get('open_ports', 0)} found)</h2>
    <table class="port-table">
        <tr><th>Port</th><th>Service</th><th>Banner</th></tr>
"""
            for port, service in sorted(data.get("ports", {}).items()):
                banner = data.get("banners", {}).get(port, "N/A")
                html += f"<tr><td>{port}/tcp</td><td>{service}</td><td>{banner}</td></tr>\n"

            html += f"""
    </table>

    <div class="footer">
        <p>ScanMos v1.0 | Educational Simulator | Author: Raj Gautam</p>
        <p style="color: #f85149; font-weight: bold;">⚠️ This is a simulated scan - no real hacking performed</p>
    </div>
</div>
</body>
</html>
"""
            with open(filename, 'w') as f:
                f.write(html)
            return True, filename
        except Exception as e:
            return False, str(e)

# ============================================================
# DISPLAY HELPERS
# ============================================================

class Display:
    """Display functions for the UI"""

    @staticmethod
    def show_dashboard():
        """Main menu dashboard"""
        Animation.clear()

        # Mini logo
        print(f"\n{Colors.RED}  ╔═══════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.RED}  ║{Colors.CYAN}   SCANMOS v1.0 - NETWORK SCANNER    {Colors.RED}║{Colors.RESET}")
        print(f"{Colors.RED}  ║{Colors.GREEN}   Educational Simulator               {Colors.RED}║{Colors.RESET}")
        print(f"{Colors.RED}  ╚═══════════════════════════════════════════╝{Colors.RESET}")

        print(f"\n{Colors.CYAN}┌─────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.YELLOW}  📌 MAIN MENU                         {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}├─────────────────────────────────────────┤{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.GREEN}  1{Colors.WHITE}. Quick Scan                    {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.GREEN}  2{Colors.WHITE}. Fast Scan                     {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.GREEN}  3{Colors.WHITE}. Deep Scan                     {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.GREEN}  4{Colors.WHITE}. Stealth Scan                  {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.GREEN}  5{Colors.WHITE}. Full Scan                     {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}├─────────────────────────────────────────┤{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.GREEN}  6{Colors.WHITE}. Scan History                  {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.GREEN}  7{Colors.WHITE}. Export Report                 {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.GREEN}  8{Colors.WHITE}. System Info                   {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.GREEN}  9{Colors.WHITE}. About / Disclaimer            {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}├─────────────────────────────────────────┤{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RED}  0{Colors.WHITE}. Exit                           {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}└─────────────────────────────────────────┘{Colors.RESET}")

    @staticmethod
    def show_result(result):
        """Display scan results"""
        Animation.clear()
        Animation.header_border('═')

        # Result header
        print(f"{Colors.GREEN}╔═══════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.GREEN}║{Colors.CYAN}  ✅ SCAN RESULTS SUMMARY                        {Colors.GREEN}║{Colors.RESET}")
        print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════╝{Colors.RESET}")

        # Host info
        print(f"\n{Colors.YELLOW}┌─ HOST INFORMATION ─────────────────────────┐{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Target      : {Colors.GREEN}{result['target']}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Status      : {Colors.GREEN}{result['status']}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Latency     : {Colors.CYAN}{result['latency']} ms{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} TTL         : {Colors.CYAN}{result['ttl']}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} MAC Address : {Colors.CYAN}{result['mac']}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Vendor      : {Colors.CYAN}{result['vendor']}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} OS          : {Colors.CYAN}{result['os']}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Uptime      : {Colors.CYAN}{result['uptime']}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Open Ports  : {Colors.CYAN}{result['open_ports']}{Colors.RESET}")
        print(f"{Colors.YELLOW}└────────────────────────────────────────────────┘{Colors.RESET}")

        # Security assessment
        rating = result['security_rating']
        score = result['security_score']
        rating_color = Colors.GREEN if "LOW" in rating else Colors.YELLOW if "MEDIUM" in rating else Colors.RED

        print(f"\n{Colors.YELLOW}┌─ SECURITY ASSESSMENT ──────────────────────┐{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Rating      : {rating_color}{rating}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Score       : {rating_color}{score}/100{Colors.RESET}")
        print(f"{Colors.YELLOW}└────────────────────────────────────────────────┘{Colors.RESET}")

        # Ports table
        if result['ports']:
            print(f"\n{Colors.YELLOW}┌─ OPEN PORTS & SERVICES ─────────────────────┐{Colors.RESET}")
            for port, service in sorted(result['ports'].items()):
                banner = result['banners'].get(port, "N/A")
                print(f"{Colors.YELLOW}│{Colors.GREEN} {port}/tcp{Colors.WHITE} - {Colors.CYAN}{service}{Colors.RESET}")
                print(f"{Colors.YELLOW}│{Colors.DIM}   {banner}{Colors.RESET}")
            print(f"{Colors.YELLOW}└────────────────────────────────────────────────┘{Colors.RESET}")

        # Footer
        print(f"\n{Colors.DIM}Scan ID: {result['scan_id']} | Duration: {result['scan_duration']}s{Colors.RESET}")
        Animation.header_border('═')

    @staticmethod
    def show_history(history):
        """Display scan history"""
        Animation.clear()

        if not history:
            print(f"{Colors.YELLOW}⚠️ No scan history found.{Colors.RESET}")
            return

        print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.GREEN}  📋 SCAN HISTORY ({len(history)} scans)             {Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════╝{Colors.RESET}")

        for idx, scan in enumerate(history, 1):
            print(f"\n{Colors.YELLOW}┌─ Scan #{idx} ─────────────────────────────────┐{Colors.RESET}")
            print(f"{Colors.YELLOW}│{Colors.WHITE} ID     : {Colors.CYAN}{scan.get('scan_id', 'N/A')}{Colors.RESET}")
            print(f"{Colors.YELLOW}│{Colors.WHITE} Target : {Colors.GREEN}{scan['target']}{Colors.RESET}")
            print(f"{Colors.YELLOW}│{Colors.WHITE} Type   : {Colors.CYAN}{scan['scan_type']}{Colors.RESET}")
            print(f"{Colors.YELLOW}│{Colors.WHITE} Status : {Colors.GREEN}{scan['status']}{Colors.RESET}")
            print(f"{Colors.YELLOW}│{Colors.WHITE} Ports  : {Colors.CYAN}{scan['open_ports']}{Colors.RESET}")
            print(f"{Colors.YELLOW}│{Colors.WHITE} Sec.   : {scan['security_rating']}{Colors.RESET}")
            print(f"{Colors.YELLOW}│{Colors.WHITE} Time   : {Colors.DIM}{scan['timestamp'][:19]}{Colors.RESET}")
            print(f"{Colors.YELLOW}└────────────────────────────────────────────────┘{Colors.RESET}")

    @staticmethod
    def show_system_info():
        """Display system information"""
        Animation.clear()
        Animation.header_border('═')

        print(f"{Colors.CYAN}╔═══════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.GREEN}  💻 SYSTEM INFORMATION                        {Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════╝{Colors.RESET}")

        print(f"\n{Colors.YELLOW}┌─ SYSTEM ──────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} OS           : {Colors.CYAN}{platform.system()} {platform.release()}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Arch         : {Colors.CYAN}{platform.machine()}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Python       : {Colors.CYAN}{platform.python_version()}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Hostname     : {Colors.CYAN}{platform.node()}{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Processor    : {Colors.CYAN}{platform.processor() or 'Unknown'}{Colors.RESET}")
        print(f"{Colors.YELLOW}└────────────────────────────────────────────────┘{Colors.RESET}")

        # ScanMos info
        print(f"\n{Colors.YELLOW}┌─ SCANMOS ────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Version      : {Colors.CYAN}1.0{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Author       : {Colors.CYAN}Raj Gautam{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} License      : {Colors.CYAN}MIT{Colors.RESET}")
        print(f"{Colors.YELLOW}│{Colors.WHITE} Type         : {Colors.CYAN}Educational Simulator{Colors.RESET}")
        print(f"{Colors.YELLOW}└────────────────────────────────────────────────┘{Colors.RESET}")

        Animation.header_border('═')

    @staticmethod
    def show_about():
        """About and disclaimer"""
        Animation.clear()
        Animation.header_border('═')

        print(f"{Colors.CYAN}╔═══════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.GREEN}  📖 ABOUT SCANMOS                           {Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════╝{Colors.RESET}")

        info = f"""
{Colors.YELLOW}┌─ GENERAL ─────────────────────────────────────┐{Colors.RESET}
{Colors.CYAN}  Name        :{Colors.WHITE} ScanMos - High-Speed Network Scanner
{Colors.CYAN}  Version     :{Colors.WHITE} 1.0
{Colors.CYAN}  Author      :{Colors.WHITE} Raj Gautam
{Colors.CYAN}  License     :{Colors.WHITE} MIT
{Colors.CYAN}  Platform    :{Colors.WHITE} Python 3.x (PyDroid, QPython, Termux)
{Colors.YELLOW}┌─ FEATURES ─────────────────────────────────────┐{Colors.RESET}
{Colors.CYAN}  •{Colors.WHITE} 5 Scan Modes (Quick, Fast, Deep, Stealth, Full)
{Colors.CYAN}  •{Colors.WHITE} Animated CLI with hacker-style UI
{Colors.CYAN}  •{Colors.WHITE} Fake but realistic scan results
{Colors.CYAN}  •{Colors.WHITE} Export to JSON, TXT, HTML
{Colors.CYAN}  •{Colors.WHITE} Scan history tracking
{Colors.CYAN}  •{Colors.WHITE} System information display
{Colors.YELLOW}┌─ DISCLAIMER ──────────────────────────────────┐{Colors.RESET}
{Colors.RED}  ⚠️  THIS IS AN EDUCATIONAL SIMULATION TOOL{Colors.RESET}
{Colors.RED}  ⚠️  Does NOT perform real network scanning{Colors.RESET}
{Colors.RED}  ⚠️  All results are randomly generated{Colors.RESET}
{Colors.RED}  ⚠️  For learning and demonstration only{Colors.RESET}
{Colors.RED}  ⚠️  Use responsibly - NO real hacking!{Colors.RESET}
{Colors.YELLOW}└────────────────────────────────────────────────┘{Colors.RESET}
"""
        print(info)
        Animation.header_border('═')

# ============================================================
# MAIN APPLICATION
# ============================================================

class ScanMosApp:
    """Main application class"""

    def __init__(self):
        self.engine = ScanEngine()
        self.running = True

    def run(self):
        """Main application loop"""
        # Show startup animation
        Logo.show_startup()
        time.sleep(0.5)

        while self.running:
            try:
                Display.show_dashboard()

                # Get user choice
                choice = input(f"\n{Colors.CYAN}└─{Colors.YELLOW} Enter your choice {Colors.GREEN}► {Colors.RESET}").strip()

                if choice == '0':
                    self.exit_app()
                elif choice == '1':
                    self.run_scan_type("Quick Scan")
                elif choice == '2':
                    self.run_scan_type("Fast Scan")
                elif choice == '3':
                    self.run_scan_type("Deep Scan")
                elif choice == '4':
                    self.run_scan_type("Stealth Scan")
                elif choice == '5':
                    self.run_scan_type("Full Scan")
                elif choice == '6':
                    Display.show_history(self.engine.history)
                    self.pause()
                elif choice == '7':
                    self.export_report()
                elif choice == '8':
                    Display.show_system_info()
                    self.pause()
                elif choice == '9':
                    Display.show_about()
                    self.pause()
                else:
                    print(f"{Colors.RED}✗ Invalid choice. Please try again.{Colors.RESET}")
                    time.sleep(0.5)

            except KeyboardInterrupt:
                self.exit_app()
            except Exception as e:
                print(f"{Colors.RED}Error: {e}{Colors.RESET}")
                self.pause()

    def run_scan_type(self, scan_type):
        """Run a specific scan type"""
        print(f"\n{Colors.CYAN}Enter target IP/host (press Enter for random):{Colors.RESET} ")
        target = input(f"{Colors.GREEN}► {Colors.RESET}").strip()
        if not target:
            target = FakeData.random_ip()
            print(f"{Colors.DIM}Using random target: {target}{Colors.RESET}")

        result = self.engine.run_scan(target, scan_type)
        Display.show_result(result)
        self.pause()

    def export_report(self):
        """Export report"""
        if not self.engine.last_result:
            print(f"{Colors.YELLOW}⚠️ No scan result to export. Run a scan first.{Colors.RESET}")
            self.pause()
            return

        print(f"\n{Colors.CYAN}Select export format:{Colors.RESET}")
        print(f"{Colors.GREEN}  1{Colors.WHITE}. JSON")
        print(f"{Colors.GREEN}  2{Colors.WHITE}. TXT")
        print(f"{Colors.GREEN}  3{Colors.WHITE}. HTML")
        print(f"{Colors.CYAN}  0{Colors.WHITE}. Cancel")

        choice = input(f"{Colors.YELLOW}► {Colors.RESET}").strip()

        format_map = {
            '1': ('json', ReportGenerator.export_json),
            '2': ('txt', ReportGenerator.export_txt),
            '3': ('html', ReportGenerator.export_html)
        }

        if choice == '0':
            return

        if choice in format_map:
            fmt, func = format_map[choice]
            success, result = func(self.engine.last_result)
            if success:
                print(f"{Colors.GREEN}✅ Report exported: {Colors.CYAN}{result}{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Export failed: {result}{Colors.RESET}")
        else:
            print(f"{Colors.RED}✗ Invalid choice.{Colors.RESET}")

        self.pause()

    def pause(self):
        """Pause and wait for user"""
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")

    def exit_app(self):
        """Exit the application"""
        print(f"\n{Colors.GREEN}┌─────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.GREEN}│{Colors.CYAN}  🔒 Exiting ScanMos... Stay Secure!{Colors.GREEN}│{Colors.RESET}")
        print(f"{Colors.GREEN}└─────────────────────────────────────┘{Colors.RESET}")
        sys.stdout.write(Colors.SHOW_CURSOR)
        self.running = False

# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    try:
        app = ScanMosApp()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠️ Interrupted.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Fatal Error: {e}{Colors.RESET}")
    finally:
        sys.stdout.write(Colors.SHOW_CURSOR)
        print(f"{Colors.DIM}Goodbye!{Colors.RESET}")
