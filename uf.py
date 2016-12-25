def union(x, y):
	xRoot = find(x)
	yRoot = find(y)

	if xRoot == yRoot:
		return

	yRoot.parent = xRoot
	xRoot.childs.append(yRoot)
	for child in yRoot.childs:
		union(xRoot, child)
		xRoot.childs.append(child)
	for child in yRoot.childs:
		yRoot.childs.remove(child)

def find(x):
	if x.parent != x:
		x.parent = find(x.parent)
	return x.parent