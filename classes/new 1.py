class ResponseFormatHelper:
	def GetHeader(self, title):
		return string.format("<header>{0}</header>", title)


	def HtmlResponse(self, message):
		return string.format("<html>{0}{1}</html>", GetHeader("Home"), message)