lastNumber = 0
countHigher = 0
inputs = open("input", "r")

for x in inputs:
	if lastNumber == 0:
		lastNumber = int(x)
	elif int(x) > lastNumber:
		countHigher+=1
		lastNumber = int(x)
	else:
		lastNumber = int(x)
print("there are " + str(countHigher) + " measurements that are larger than the previous measurement")