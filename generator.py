from maze import Maze
from index import Index
from random import randint, choice

class Generator(object):
	direita = 0
	baixo = 1
	esquerda = 2
	cima = 3

	def gerar(linhas, colunas):
		maze = Maze(linhas, colunas)
		
		while not(maze.connected()):
			index1 = Index(randint(0, linhas-1), randint(0, colunas-1))
			index2 = Index(index1.linha, index1.coluna)
			
			validos = [Generator.direita, Generator.baixo, Generator.esquerda, Generator.cima]

			if index1.linha == 0:
				validos.remove(Generator.cima)
			elif index1.linha == linhas-1:
				validos.remove(Generator.baixo)

			if index1.coluna == 0:
				validos.remove(Generator.esquerda)
			elif index1.coluna == colunas-1:
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

			print(index1)
			print(index2)
			maze.conectar(index1, index2)

		print(maze)
		
	def __init__(self):
		super(Generator, self).__init__()	

Generator.gerar(12, 12)