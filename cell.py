class Cell(object):
	identificador = 1
	def __init__(self):
		super(Cell, self).__init__()
		self.id = Cell.identificador
		self.parent = self	
		self.childs = []
		self.reset_string()
		Cell.identificador += 1	

	def reset_string(self):
		self.top = '<->'
		self.mid = '| |'
		self.bot = '<->'

	def abrir_bot(self):
		self.bot = '< >'

	def abrir_top(self):
		self.top = '< >'

	def abrir_direita(self):
		if self.mid == '| |':
			self.mid = '|  '
		elif self.mid == '  |':
			self.mid = '   '

	def abrir_esquerda(self):
		if self.mid == '| |':
			self.mid = '  |'
		elif self.mid == '|  ':
			self.mid = '   '

	def __str__(self):
		return str(self.id)+"|"+str(self.parent.id)