# DDoS Attack Simulator

## Overview
This project simulates a Distributed Denial of Service (DDoS) attack on a web server using Python. The goal is to send a flood of HTTP requests to the target server to overwhelm it, and observe the network behavior using Wireshark.

## Project Structure
- **ddos_simulator.py**: Python script that simulates the DDoS attack by creating multiple threads that flood the target server with HTTP requests.
- **index.html**: Simple web page that will serve as the target for the DDoS attack (using XAMPP or other local server).

## Setup Instructions

### 1. Install Required Software
- **Python**: Install Python from [python.org](https://www.python.org/downloads/).
- **Wireshark**: Install Wireshark from [Wireshark download](https://www.wireshark.org/download.html).
- **XAMPP** (optional, for local web server): Download from [XAMPP](https://www.apachefriends.org/index.html).

### 2. Prepare the Target Web Server
1. Install **XAMPP** and start Apache.
2. Navigate to `C:\xampp\htdocs\` and create a simple `index.html` file with the content provided in the project.
3. Ensure the server is running by opening `http://localhost/` in a web browser.

### 3. Run the DDoS Attack
1. Save the Python script `ddos_simulator.py` on your machine.
2. Open a terminal and run the following command:

   ```bash
   python ddos_simulator.py

### 4. Capture Traffic with Wireshark
Open Wireshark.

Start capturing on the network interface.

Apply the filter to capture relevant traffic:

 tcp.port == 80
Observe the traffic flooding the target server from your local machine.