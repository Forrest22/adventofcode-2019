import csv

dictX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
dictY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

def getwires():
	wires = []
	with open('input.txt') as fp:
		reader = csv.reader(fp)
		for line in reader:
			wires.append([i for i in list(line)])
	return wires

def plot(wire):
	x = 0
	y = 0
	length = 0
	ans = {}

	for cmd in wire:
		direction = cmd[0]
		num = int(cmd[1:])
		for i in range(num):
			x += dictX[direction]
			y += dictY[direction]
			# ans.add((x,y))
			length += 1
			if (x,y) not in ans:
				ans[(x,y)] = length
	return ans


if __name__ == '__main__':
	# print(len(getwires()))
	wires = getwires()
	points = []
	for wire in wires:
		points.append(plot(wire))

	intersect = set(points[0].keys()).intersection(set(points[1].keys()))
	print(intersect)

	#now for part 2 where we care about which intersection is the most efficient
	# part1 = min([abs(x)+abs(y) for (x,y) in intersect])
	# print(part1)
	part2 = min([points[0][point]+points[1][point] for point in intersect])
	print(part2)