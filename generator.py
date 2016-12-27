from maze import Maze
from index import Index
from uf import find
from random import randint, choice

class Generator(object):
	direita = 0
	baixo = 1
	esquerda = 2
	cima = 3
		
	def __init__(self, linhas, colunas):
		super(Generator, self).__init__()	
		self.linhas = linhas
		self.colunas = colunas
		self.maze = Maze(self.linhas, self.colunas)

	def celulas_desconexas(self):
		roots = []
		lista = []

		for i in range(0, self.linhas):
			for cell in self.maze.mapa[i]:
				roots.append(find(cell))

		for i in range(0, len(roots)):
			for j in range(i+1, len(roots)):
				if roots[i] != roots[j] and not(roots[i].index in lista):
					lista.append(roots[i].index)
				elif roots[i] != roots[j] and not(roots[j].index in lista):
					lista.append(roots[j].index)

		return lista

	def gerar(self):
		lista = []

		while not(self.maze.connected()):
			# index1 = Index(randint(0, linhas-1), randint(0, colunas-1))
			lista = self.celulas_desconexas()

			index1 = choice(lista)

			index2 = Index(index1.linha, index1.coluna)
			
			validos = [Generator.direita, Generator.baixo, Generator.esquerda, Generator.cima]

			if index1.linha == 0:
				validos.remove(Generator.cima)
			elif index1.linha == self.linhas-1:
				validos.remove(Generator.baixo)

			if index1.coluna == 0:
				validos.remove(Generator.esquerda)
			elif index1.coluna == self.colunas-1:
				validos.remove(Generator.direita)

			direcao = choice(validos)
			if direcao == Generator.direita:
				index2.coluna += 1
			elif direcao == Generator.baixo:
				index2.linha += 1
			elif direcao == Generator.esquerda:
				index2.coluna -= 1
			elif direcao == Generator.cima:
				index2.linha -= 1

			self.maze.conectar(index1, index2)

generator = Generator(4, 4)
generator.gerar()
generator.maze.print_c()
print(generator.maze)