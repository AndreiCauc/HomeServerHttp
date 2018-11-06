from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import log
import ResponseFormatHelper

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
		input = self.path.split("/")
		log.error("Path", self.path);
		try:
			service_name = input[1]
			function_name = input[2]
			args = ""
			if len(input) > 3:
				for i in range(3, len(input)):
					args += "/{}".format(input[i])
				
			return self.wfile.write(self.CallService(service_name, function_name, args))
		except:
			log.error("Connection", "The input is wrong")
		
		return self.wfile.write(ResponseFormatHelper.HtmlResponse("<html><body><h1>404 NOT FOUND!</h1></body></html>"))

	def do_HEAD(self):
		self._set_headers()

	def do_POST(self): 
		# Doesn't do anything with posted data
		self._set_headers()
		self.wfile.write("<html><body><h1>Under construction!</h1></body></html>")
		
		
		
	def CallService(self, service_name, service_function, args):
		if args != "":
			args = args[1:]
		
		service = None
		try:
			service = __import__("{}.service".format(service_name)).service.service()
		except:
			return ResponseFormatHelper.HtmlResponse("Wrong Service");
			
		#try:
		method = getattr(service, service_function)
		args = args.split("/")
		if args[0] != "":
			res = method(*args)
			return res
		else:
			res = method()
			return res
		#except:
		#	log.error("Server", "Function name is incorrect.")
		#	return ResponseFormatHelper.HtmlResponse("Incorrect format");
