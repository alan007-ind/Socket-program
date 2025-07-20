from http.server import HTTPServer, BaseHTTPRequestHandler
import time  # Optional: you can simulate a slow server by using sleep()

PORT = 8888


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Log attacker/client IP and port
        print(f"[+] GET from {self.client_address[0]}:{self.client_address[1]}")

        # Optional: simulate server slowness to stress test DoS attack
        # time.sleep(0.2)

        # Send a basic response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello from LAHTP HTTP Server!")

    def log_message(self, format, *args):
        # Disable default logging (optional)
        return


if __name__ == "__main__":
    print(f"[+] LAHTP HTTP Server is listening on port {PORT}")
    httpd = HTTPServer(('0.0.0.0', PORT), SimpleHTTPRequestHandler)
    httpd.serve_forever()
