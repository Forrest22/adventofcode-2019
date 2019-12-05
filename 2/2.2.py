import csv

def calculateresult(opcode, var1, var2):
	# print(opcode,var1,var2)
	if opcode == 1:
		result = var1 + var2
	elif opcode == 2:
		result = var1 * var2
	else:
		raise Exception("Opcode \"" + str(opcode) + "\" is funky!")
	return result

def evalinstruction(instruc, position):
	print(instruc)
	opcode = int(instruc[position])
	var1 = instruc[int(instruc[position+1])]
	var2 = instruc[int(instruc[position+2])]
	resultpos = instruc[position+3]

	instruc[resultpos] = calculateresult(opcode, var1, var2)
	return instruc

instructions = []
with open('input.txt') as fp:
	reader = csv.reader(fp)
	instructions = [int(i) for i in list(reader)[0]]

# replace position 1 with the value 12 and replace position 2 with the value 2
instructions[1] = 12
instructions[2] = 2

position = 0
while position < len(instructions) - 4:
	print(instructions[position], instructions[position+1], instructions[position+2], instructions[position+3])
	if instructions[position] != 99:
		print("not 99")
		storeinpos = int(instructions[position+3])
		instructions = evalinstruction(instructions, position)

	position += 4

print(instructions[0])