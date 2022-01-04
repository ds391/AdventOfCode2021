file = open("input", "r")
inputs = (file.read().split("\n"))
inputs = map(int,inputs)
lastNumber = 0
countHigher = 0
x = 0
print(len(inputs))
while x < len(inputs)-2:
	print(x)
	y = inputs[x]+inputs[x+1]+inputs[x+2]
	if lastNumber == 0:
		lastNumber = int(x)
	elif int(x) > lastNumber:
		countHigher+=1
		lastNumber = int(x)
	else:
		lastNumber = int(x)
	x+=1
	
print("there are " + str(countHigher) + " measurements that are larger than the previous measurement")