from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class ServerHandler(BaseHTTPRequestHandler):
	def _set_headers(self):
        	self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		self._set_headers()
		#first argument = service name
		#second argument = service function
		#third+ args = args
		respPath = self.path;
		self.wfile.write("<html><body><h1>" + 
						 "hi!" + 
						 respPath +
						 "</h1></body></html>")

	def do_HEAD(self):
		self._set_headers()

	def do_POST(self):
		# Doesn't do anything with posted data
		self._set_headers()
		self.wfile.write("<html><body><h1>Under construction!</h1></body></html>")