import time
import SimpleHTTPServer
import SocketServer
from ServerHandler import ServerHandler
import log

class server(object):
	def __init__(self, PORT, services_array, timeout):
		self._PORT = PORT
		self._ServerOn = False
		self._services = {}
		self._services_array = services_array
		self._timeout = timeout

	@property
	def ServerOn(self):
		return self._ServerOn

	@property
	def Services(self):
		return self._services

	def StartServer(self):
		self._ServerOn = True
		httpd = SocketServer.TCPServer(("", self._PORT), ServerHandler)
		log.success("Server", "Server is on [{0}]".format(self._PORT));
		httpd.serve_forever()
		return

	def CloseServer(self):
		self._ServerOn = False
