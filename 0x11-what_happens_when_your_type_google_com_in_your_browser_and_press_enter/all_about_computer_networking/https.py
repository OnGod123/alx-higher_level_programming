import http.server
import ssl

class MyHTTPSServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Hello, HTTPS/SSL!</h1>")

server_address = ('localhost', 443)

httpd = http.server.HTTPServer(server_address, MyHTTPSServer)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)

print("Server running at https://localhost:443/")
httpd.serve_forever()

