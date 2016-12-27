from cell import Cell
from index import Index
from uf import *

class Maze(object):
	def __init__(self, linhas, colunas):
		super(Maze, self).__init__()
		self.linhas = linhas
		self.colunas = colunas
		self.mapa = [[Cell(Index(y, x)) for x in range(colunas)] for y in range(linhas)]
		
	def connected(self):
		roots = []
		for i in range(0, self.linhas):
			for cell in self.mapa[i]:
				roots.append(find(cell))

		for i in range(0, len(roots)):
			for j in range(i+1, len(roots)):
				if roots[i] != roots[j]:
					return False
		return True

	def conectar(self, index_1, index_2):
		celula_1 = self.mapa[index_1.linha][index_1.coluna]
		celula_2 = self.mapa[index_2.linha][index_2.coluna]

		union(celula_1, celula_2)

		if index_1.linha < index_2.linha:
			# celula_1 esta em cima
			self.mapa[index_1.linha][index_1.coluna].abrir_bot()
			self.mapa[index_2.linha][index_2.coluna].abrir_top()
		elif index_1.linha > index_2.linha:
			# celula_1 esta em baixo
			self.mapa[index_1.linha][index_1.coluna].abrir_top()
			self.mapa[index_2.linha][index_2.coluna].abrir_bot()
		elif index_1.coluna < index_2.coluna:
			# celula_1 esta a esquerda
			self.mapa[index_1.linha][index_1.coluna].abrir_direita()
			self.mapa[index_2.linha][index_2.coluna].abrir_esquerda()
		elif index_1.coluna > index_2.coluna:
			# celula_1 esta a direita
			self.mapa[index_1.linha][index_1.coluna].abrir_esquerda()
			self.mapa[index_2.linha][index_2.coluna].abrir_direita()

	def print_c(self):
		for i in range(0, self.linhas):
			for cell in self.mapa[i]:
				print(str(cell)+', ', end='')
			print('')

	def __str__(self):
		string = ''
		for i in range(0, self.linhas):
			if i == 0:
				for j in range(0, self.colunas):
					# print(self.mapa[i][j].top, end='')
					string += self.mapa[i][j].top
				# print('')
				string += '\n'
			for j in range(0, self.colunas):
				# print(self.mapa[i][j].mid, end='')
				string += self.mapa[i][j].mid
			# print('')
			string += '\n'
			for j in range(0, self.colunas):
				# print(self.mapa[i][j].bot, end='')
				string += self.mapa[i][j].bot
			# print('')
			string += '\n'
		return string

# maze = Maze(12, 12)

# for i in range(0, 12):
# 	for j in range(1, 12):
# 		maze.conectar(Index(i, j-1), Index(i, j))

# for i in range(1, 12):
# 	maze.conectar(Index(i-1, 0), Index(i, 0))
# maze.print_c()
# print(maze)
# print(maze.connected())