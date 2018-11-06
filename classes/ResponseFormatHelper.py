def GetHeader(title):
	return "<header><title>{0}</title></header>".format(title)


def HtmlResponse(message):
	return "<html>{0}{1}</html>".format(GetHeader("Home"), message)