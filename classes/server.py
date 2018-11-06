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
		print "Server listening at ", self._PORT
		httpd.serve_forever()

		#initializing services
		log.success("Server", "Initalizing services")
		for string in self._services_array:
			self._services[string] = __import__("{}.service".format(string)).service.service()

		log.success("Server", "Server is on")
		return

	def CloseServer(self):
		self._ServerOn = False
