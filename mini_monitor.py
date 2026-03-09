import pandas
import subprocess
from datetime import datetime
import re
import time
import requests 

server_list = "Your CSV Server list"
log = "Your empty CSV file for logging"
topic = "Your ntfy key"

session_log_m = []
dataset = pandas.read_csv(server_list)

def alert(message, priority="default"):
    requests.post(f"https://ntfy.sh/{topic}", data=message.encode(encoding="utf-8"),
    headers = {
        "Title": "Server failure!",
        "Priority": priority,
        "Tags": "triangular_flag_on_post"
    })

def get_output(output):
    time_match = re.search(r"time=([\d\.]+) ms", output)
    if time_match:
        latency = time_match.group(1)
    else:
        latency = "N/A"
        
    loss_match = re.search(r"(\d+)% packet loss", output)
    if loss_match:
        loss = loss_match.group(1) 
    else: 
        loss = "100"
        
    return latency, loss

def status(server_hostname,result):
    
    if result.returncode == 0:
        print(f"{server_hostname} is currently online.\n")
    else:
        print(f"{server_hostname} is currently offline.\n")
        # Keep a list of offline servers for messaging.
        if server_hostname not in session_log_m:
            session_log_m.append(server_hostname)

def health_check():
    session_log = []
    session_log_m.clear()
    
    print("Starting...")
    for hostname,server in zip(dataset["Server Name"], dataset["IP"]):
        result = subprocess.run(["ping","-n", "3", "-w", "1", server], capture_output=True, text=True)
        status(hostname,result)
        
        #logs general performance at x interval on paper##
        latency, loss = get_output(result.stdout)
        
        session_log.append({
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Hostname": hostname,
            "IP": server,
            "Status": "Online" if result.returncode == 0 else "Offline",
            "Latency_ms": latency,
            "Packet_Loss_Pct": loss
        })
        session_log_ex = pandas.DataFrame(session_log)
        session_log_ex.to_csv(log, index=False)
        #end of logging

    if session_log_m:
        alert(f"The following servers are down:\n {", ".join(session_log_m)}", priority="high")

    print("End of Session")
    
while True:
    health_check()
    ## checks every 6hrs
    time.sleep(21600)