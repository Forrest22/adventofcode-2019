import csv

def getwires():
	wires = []
	with open('test.txt') as fp:
		reader = csv.reader(fp)
		for line in reader:
			wires.append([i for i in list(line)])
	return wires

def getnextcorner(edge, start):
	nextcoord = []
	length = int(edge[1:])
	if edge[0] == "R":
		# print("R")
		nextcoord = [start[0]+length,start[1]]
	elif edge[0] == "L":
		# print("L")
		nextcoord = [start[0]-length,start[1]]
	elif edge [0] == "U":
		# print("U")
		nextcoord = [start[0],start[1]+length]
	elif edge[0] == "D":
		# print("D")
		nextcoord = [start[0],start[1]-length]

	return nextcoord

def getwirecoords(wire):
	coords = [[0,0]]
	for edge in wire:
		currentcoords = coords[len(coords)-1]
		# print(edge, currentcoords)
		coords.append(getnextcorner(edge,currentcoords))
	return coords

def getwiredimensions(wires):
	xmin = wires[0][0][0]
	xmax = wires[0][0][0]
	ymin = wires[0][0][1]
	ymax = wires[0][0][1]
	
	for coords in wires:
		for coordinate in coords:
			if coordinate[0] < xmin:
				xmin = coordinate[0]
			elif coordinate[0] > xmax:
				xmax = coordinate[0]
			elif coordinate[1] < ymin:
				ymin = coordinate[1]
			elif coordinate[1] > ymax:
				ymax = coordinate[1]
	print(xmin,xmax)
	print(ymin,ymax)

	return [[xmin,xmax],[ymin,ymax]]

def plotcoords(wirenum, wires):
	plotsize = getwiredimensions(wires)
	# plot = [0 for x in range(xmin,xmax)]
	plot = [[0 for i in range(plotsize[0][0],plotsize[0][1])] for j in range(plotsize[1][0],plotsize[1][1])]

	currentcoord = wires[0][0]

	for wire in wires:
		for coordinate in wire:
			
			for x in range(currentcoord,coordinate):
				plot(x)


	for row in plot:
		print(row)


if __name__ == '__main__':
	# print(len(getwires()))
	wires = getwires()
	coords = []
	for i, wire in enumerate(wires):
		coords.append(getwirecoords(wire))
		# print(i, coords)
	plotcoords(i, coords)