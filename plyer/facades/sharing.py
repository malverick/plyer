class Sharing(object):
	'''
	Sharing facade.
	'''

	def share(self, text):
		return self._share()

	#private

	def _share(self, text):
		raise NotImplementedError()
