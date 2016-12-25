def union(x, y):
	xRoot = find(x)
	yRoot = find(y)

	if xRoot == yRoot:
		return

	if xRoot.rank < yRoot.rank:
		xRoot.parent = yRoot
		yRoot.rank += 1
	elif xRoot.rank >= yRoot.rank:
		yRoot.parent = xRoot
		xRoot.rank += 1

def find(x):
	if x.parent != x:
		x.parent = find(x.parent)
	return x.parent