from collections import Counter
file = open("input", "r")
inputs = list(file.read().splitlines())
rows = len(inputs)
columns = len(inputs[0])
gamma = []
epsilon = []
loop = 0

def common(arrayLocation, frequency):
	value = 0
	for x in inputs:
		if int(x[arrayLocation]) > 0:
			value +=1
		else:
			value -=1
	if frequency == "least":
		if value > 0:
			return 0
		else: 
			return 1
	elif frequency == "most":
		if value > 0:
			return 1
		else:
			return 0

