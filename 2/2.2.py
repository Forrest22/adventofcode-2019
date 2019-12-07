import csv

# given opcode and 2 resulting values calculates and the returns result
def calculateresult(opcode, parm1, parm2):
	# print(opcode,parm1,parm2)
	if opcode == 1:
		result = parm1 + parm2
	elif opcode == 2:
		result = parm1 * parm2
	else:
		raise Exception("Opcode \"" + str(opcode) + "\" is funky!")
	return result

#readsd the opcode at position, calculates the result, and stores the value
def evalinstruction(instruc, position):
	# print(instruc)
	opcode = int(instruc[position])
	parm1 = instruc[int(instruc[position+1])]
	parm2 = instruc[int(instruc[position+2])]
	resultpos = instruc[position+3]

	instruc[resultpos] = calculateresult(opcode, parm1, parm2)
	return instruc

# reads the values
def getinstructions():
	instructions = []
	with open('input.txt') as fp:
		reader = csv.reader(fp)
		instructions = [int(i) for i in list(reader)[0]]
	return instructions

# get noun and verb
def getnoun(n=False):
	# print (n)
	if isinstance(n,int):
		return n
	else:
		print("Noun:")
		noun = input()
		return noun

def getverb(v=False):
	# print(v)
	if isinstance(v,int):
		return v
	else:
		print("Verb:")
		verb = input()
		return verb

def runinstructions(n = False, v = False):
	# print(n,v)
	instructions = getinstructions()
	noun = getnoun(n)
	verb = getverb(v)

	# replace position 1 with the value 12 and replace position 2 with the value 2
	instructions[1] = noun
	instructions[2] = verb

	#loops through opcode positions
	instructionpointer = 0
	while instructionpointer < len(instructions) - 4:
		# print(instructions[instructionpointer], instructions[instructionpointer+1], instructions[instructionpointer+2], instructions[instructionpointer+3])
		if instructions[instructionpointer] != 99:
			# print("not 99")
			storeinpos = int(instructions[instructionpointer+3])
			instructions = evalinstruction(instructions, instructionpointer)

		instructionpointer += 4

	# prints the answer
	# print(instructions[0])
	return instructions[0]

if __name__ == '__main__':
	# runinstructions(12,2)
	print(100*76+21)
	# for n in range(-100,100):
	# 	for v in range(-100, 100):
	# 		if runinstructions(n,v) == 19690720:
	# 			print(n,v)