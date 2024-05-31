from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Server(BaseHTTPRequestHandler):

    def _set_headers(self, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self._set_headers(content_type='application/json')
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self._set_headers()
            self.wfile.write(b'OK')
        else:
            self._set_headers()
            self.wfile.write(b'Endpoint not found')


def run(server_class=HTTPServer, handler_class=Server,
        port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
