import subprocess
import platform
import json
import time
from server_manager import *

# Bestandsnaam voor loggegevens
LOG_DATA_FILE = "log.json"

def load_log():
    try:
        with open(LOG_DATA_FILE, "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_log(log_entry):
    log = load_log()
    log.append(log_entry)
    with open(LOG_DATA_FILE, "w") as file:
        json.dump(log, file, indent=4)

def ping(naam, ip):
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    command = ["ping", parameter, "1", ip]
    response = subprocess.call(command)

    if response == 0:
        ping_result = "Up"
    else:
        ping_result = "Down"
    
   
    log_entry = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "server_name": naam,
            "server_address": ip,
            "ping_result": ping_result,
        }
    save_log(log_entry)
    return ping_result



def generate_html_report():
    log = load_log()

    html_report = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Network Monitoring Report</title>
        <link rel="stylesheet" href="style.css"/>
    </head>
    <body>
        <table border="1">
            <tr>
                <th>Timestamp</th>
                <th>Server Name</th>
                <th>Server Address</th>
                <th>Ping Result</th>
            </tr>
    """

    for entry in log:
        html_report += f"""
            <tr>
                <td>{entry['timestamp']}</td>
                <td>{entry['server_name']}</td>
                <td>{entry['server_address']}</td>
                <td>{entry['ping_result']}</td>
            </tr>
        """

    html_report += """
        </table>
    </body>
    </html>
    """

    with open("report.html", "w") as file:
        file.write(html_report)

if __name__ == "__main__":
    # Voer pings uit voor geregistreerde servers en sla de resultaten op
    servers = load_servers()  # Laad servers vanuit server_manager.py
    for server in servers:
        ping_result = ping(server["name"], server["address"])
        print(f"Ping result for {server['name']} ({server['address']}):")
        print(ping_result)

    generate_html_report()
    print("HTML report generated: report.html")
