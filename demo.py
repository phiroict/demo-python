import http.server
import socketserver

PORT=10000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as http:
    print("Serving port: ", PORT )
    http.serve_forever()