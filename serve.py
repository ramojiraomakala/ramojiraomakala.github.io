import http.server
import os
import socketserver

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 4321
with socketserver.TCPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"serving portfolio on http://127.0.0.1:{PORT}")
    httpd.serve_forever()
