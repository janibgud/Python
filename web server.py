import os
import urllib.parse
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path != '/':
            # Extract directory path from request
            path = os.path.abspath(urllib.parse.unquote(self.path[1:]))
            # If the path is a file and not a folder
            if os.path.isfile(path):
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Disposition', 'attachment; filename=' + os.path.basename(path))
                self.end_headers()
                try:
                    with open(path, 'rb') as f:
                        self.wfile.write(f.read())
                except ConnectionAbortedError:
                    print("connection closed by client")
                return
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            try:
                # Check if path is a valid directory
                if os.path.isdir(path):
                    # Get directory listing
                    dir_listing = os.listdir(path)
                    # Convert directory listing to string with download links
                    dir_listing_str = ""
                    for file in dir_listing:
                        if os.path.isfile(os.path.join(path, file)):
                            # encode the file name in case it has spaces
                            encoded_file = urllib.parse.quote(file)
                            dir_listing_str += f'<a href="{path}/{encoded_file}" download>{file}</a> <br>'
                        else:
                            dir_listing_str += file + "<br>"
                    self.wfile.write(bytes(dir_listing_str, 'utf8'))
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes("Error: Not a valid directory", 'utf8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("Error: " + str(e), 'utf8'))
    def do_POST(self):
        if self.path == "/cmd":
            content_length = int(self.headers['Content-Length'])
            cmd = self.rfile.read(content_length).decode()
            try:
                # Run command and capture output
                output = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                # Send output to client
                self.wfile.write(bytes(output.stdout.decode(), 'utf8'))
                self.wfile.write(bytes(output.stderr.decode(), 'utf8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("Error: " + str(e), 'utf8'))

def run():
    print('starting server...')
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()
