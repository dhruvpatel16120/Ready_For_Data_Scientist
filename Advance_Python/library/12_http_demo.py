import http.client
import http.server
import socketserver
import threading
import time

"""
Python http Module
Provides HTTP client and server functionality.
"""

# 1. HTTP Client Example
print("--- HTTP Client Demo ---")
conn = http.client.HTTPSConnection("www.google.com")
conn.request("GET", "/")
r1 = conn.getresponse()
print(f"Status: {r1.status}, Reason: {r1.reason}")
data1 = r1.read()
print(f"Data size: {len(data1)} bytes")
conn.close()

# 2. HTTP Server Example (Minimal)
# We'll run a server in a separate thread and stop it quickly.
PORT = 8000

class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return # Suppress logs for demo

def run_server():
    with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
        print(f"\nServing at port {PORT}")
        httpd.serve_forever()

# For a real demonstration, you would run this and visit localhost:8000
# print("\nStarting a temporary server thread...")
# daemon_thread = threading.Thread(target=run_server, daemon=True)
# daemon_thread.start()
# time.sleep(1)
# print("Server is running on background...")
# print("In reality, you'd use 'python -m http.server' for quick hosting.")
