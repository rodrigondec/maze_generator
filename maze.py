from cell import Cell
from index import Index
from uf import *

class Maze(object):
	def __init__(self, linhas, colunas):
		super(Maze, self).__init__()
		self.linhas = linhas
		self.colunas = colunas
		self.mapa = [[Cell() for x in range(colunas)] for y in range(linhas)]
		
	def connected(self):
		roots = []
		for i in range(0, linhas):
			for cell in maze[i]:
				roots.append(find(cell))

		for root_1 in roots:
			for root_2 in roots:
				if root_1 != root_2:
					return False
		return True

	def conectar(self, index_1, index_2):
		if index_1.linha
		celula_1 = self.mapa[index_1.linha][index_1.coluna]
		celula_2 = self.mapa[index_2.linha][index_2.coluna]

		union(celula_1, celula_2)

		if index_1.linha <

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


# for i in range(0, linhas):
# 	for cell in maze[i]:
# 		print(find(cell).id)

# print_m(maze, linhas, colunas)

