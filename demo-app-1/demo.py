import http.server
import socketserver
import requests

DEP_SERVICE="demo-app-2"
DEP_SERVICE_PORT = 10010

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = 'webpage.html'
        response = requests.get("http://{}:{}".format(DEP_SERVICE, DEP_SERVICE_PORT))
        print("Return value is : {}".format(response.text) )
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 10000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()