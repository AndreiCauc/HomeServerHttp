import sys

sys.path.append('classes/')
sys.path.append("services/")

import SimpleHTTPServer
import SocketServer
import server



config_array = ["timer", "lighting", "water"]

PORT = 8080
myServer = server.server(PORT, config_array, 0)

exit = 0
while exit == 0:
	print("0 EXIT")
	print("1 Start Server")
	print("2 Close Server")
	print("3 Close connections")
	print("4 Send Message to all connections")
	print("5 Display RPi informations")

	var = raw_input("What to do \n")

	if (not var or int(var) == 0):
		if myServer.ServerOn == True:
			myServer.CloseServer()

		exit = 1

	elif (int(var) == 1):
		#screen.print_message("Server", "Server is up")
		myServer.StartServer() #create thread on the server to accept connections
	elif (int(var) == 2):
		#screen.print_message("Server", "Server is closed")
		myServer.CloseServer()
	elif (int(var) == 4):
		myServer.TestLocate()
	elif (int(var) == 5):
		rpt.getCPUuse()
		rpt.getCPUtemperature()
		rpt.getRAMinfo()
		rpt.getDiskSpace()
