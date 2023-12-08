from http.server import SimpleHTTPRequestHandler
import http.server
import socketserver

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

PORT = 8000

Handler = CORSRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at http://localhost:{PORT}")
httpd.serve_forever()