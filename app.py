import os  # pr hello change v2
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = os.environ.get("APP_VERSION", "dev")
PORT = int(os.environ.get("PORT", "8080"))  # pr demo tweak

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f'{{"app": "demo-api", "version": "{VERSION}"}}'.encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass

if __name__ == "__main__":
    print(f"demo-api {VERSION} listening on :{PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
