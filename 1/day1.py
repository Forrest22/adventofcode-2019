import math

# to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
def calculatefuel(mass):
	if mass < 6:
		return 0

	fuelneeded = math.floor(mass / 3) - 2
		
	if fuelneeded > 6:
		fuelneeded += calculatefuel(fuelneeded)
	
	return fuelneeded

total = 0
with open('input.txt') as fp:
	for line in fp:
		line = int(line)
		total += calculatefuel(line)

print(total)