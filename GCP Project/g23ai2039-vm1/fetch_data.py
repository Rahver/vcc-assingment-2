#!/usr/bin/python3
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Fetch data from VM2
        command = "ssh -i ~/gcp/gcp g23ai2039-vm2@10.128.0.3 'database.db \"SELECT * FROM users1;\"'"
        result = subprocess.getoutput(command)

        # Prepare the HTTP response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Database Records</h1><pre>")
        self.wfile.write(result.encode('utf-8'))
        self.wfile.write(b"</pre></body></html>")

# Set up and start the HTTP server
server_address = ('', 80)
httpd = HTTPServer(server_address, RequestHandler)
print('Running server on port 80...')
httpd.serve_forever()
