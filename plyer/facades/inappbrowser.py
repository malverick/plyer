class InAppBrowser(object):
	'''
	In App Browser facade.
	'''

	def load_page(self):
		return _load_page()

	def reload(self):
		return _reload()

	def go_back(self):
		return _go_back()

	def go_forward(self):
		return _go_forward()

	#private

	def _load_page(self):
		raise NotImplementedError()

	def _reload(self):
		raise NotImplementedError()

	def _go_back(self):
		raise NotImplementedError()

	def _go_forward(self):
		raise NotImplementedError()
