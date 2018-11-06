class service(object):
	def __init__(self):
		print("Init service lighting")	

	def test2(self):
		print("We are in the function")	
		return "<html><body><h1>Lighting module!</h1></body></html>";
	
	def test(self, param1, param2):
		return("Lighting module! {}, {}".format(param1, param2))

	def CloseService(self):
		print("Closed lighting module")
