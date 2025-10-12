from http.server import BaseHTTPRequestHandler, HTTPServer
from cache_manager import fetch_response, invalidate_cache
import requests


class CachingProxyHandler(BaseHTTPRequestHandler):
    origin = None  # set dynamically

    def do_GET(self):

        if self.path == "/clear-cache":
            invalidate_cache()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Cache cleared")
            return

        target_url = f"{self.origin}{self.path}"
        try:
            #Get the response data
            response_data = fetch_response(target_url)

            # Send response
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response_data.encode())
        except requests.RequestException as e:
            self.send_error(502, f"Bad Gateway: {e}")


def run_server(port, origin):
    """
    Run the HTTPServer forever.
    :param port: Is the port number to make the connection.
    :param origin: Is the base url.
    """

    CachingProxyHandler.origin = origin
    server = HTTPServer(('localhost', port), CachingProxyHandler)
    print(f"🚀 Caching proxy started on port {port}")
    print(f"🔗 Forwarding requests to {origin}")
    server.serve_forever()


def empty_cache():
    """Clear all the response store in cache"""

    requests.get("http://localhost:3000/clear-cache")





