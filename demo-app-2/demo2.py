import http.server
import socketserver
import json


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        r = {}
        r["bla"] = "bli"
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()        
        ret_val = json.dumps(r, indent=2)
        self.wfile.write(str.encode(ret_val))        
        

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 10010
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()