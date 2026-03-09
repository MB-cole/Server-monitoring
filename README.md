# Server-monitoring
A lightweight Python-based monitoring tool designed to check server uptime and network performance while also notifying the user of server downtime across a virtualized environment.

## 🚀 Overview
This project simulates a "data center environment" using **Vagrant** and uses **Python** to ensure all nodes are responding within acceptable latency thresholds.

## 🛠️ Stack
* **Orchestration:** Vagrant (Ubuntu 22.04 nodes)
* **Virtualization:** VirtualBox
* **Language:** Python 3
* **Libraries:** Pandas (Data Handling), Subprocess (Network Diagnostics), Requests (API Integration)
* **Alerting:** [ntfy.sh](https://ntfy.sh/) (Push Notifications)

## 📋 Key Features
* **Automated ICMP Checks:** Uses the `subprocess` module to ping a list of server IPs defined in a CSV.
* **Telemetry Extraction:** Employs Regex to parse latency (ms) and packet loss percentages from raw system output.
* **Persistent Logging:** Automatically generates/updates a log file with timestamps for historical performance tracking.
* **Alerting:** Integrated with the ntfy.sh REST API to send push notifications if a server failure/ shutdown is detected.

## 📂 Project Structure
* `Vagrantfile`: Defines the virtualized server environment.
* `mini_monitor.py`: The core Python logic for health checks and alerting.
* `Server_list.csv`: The inventory of hostnames and IP addresses to monitor.
* `log.csv`: Historical uptime/downtime data.

## ⚙️ Configuration & Setup
1. **Prepare your files:**
   Update the following variables in `monitor.py` with your specific file paths and API key:
   * `sever_list`: Path to your CSV containing "Server Name" and "IP" columns.
   * `log`: Path to your CSV file for logging output.
   * `topic`: Your unique ntfy.sh subscription key.

2. **Initialize Environment:**
   ```bash
   # Start your virtual servers
   vagrant up
