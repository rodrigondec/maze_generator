class Index(object):
	def __init__(self, linha, coluna):
		super(Index, self).__init__()
		self.linha = linha
		self.coluna = coluna

	def __str__(self):
		return "["+str(self.linha)+"]["+str(self.coluna)+"]"