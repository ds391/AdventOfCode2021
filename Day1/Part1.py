import os
if os.path.exists("output"):
	os.remove("output")
lastNumber = 0
countHigher = 0
output = open("output", "w")
inputs = open("input", "r")

for x in inputs:
	if lastNumber == 0:
		#output.write(str(x).rstrip() + "(N/A - no previous measurement)\n")
		lastNumber = int(x)
	elif int(x) > lastNumber:
		#output.write( str(x).rstrip() + "(increased)\n")
		countHigher+=1
		lastNumber = int(x)
	else:
		#output.write(str(x).rstrip() + "(decreased)\n")
		lastNumber = int(x)
#output.write("there are " + str(countHigher) + " measurements that are larger than the previous measurement")
print(lastNumber)
print(countHigher)
print("there are " + str(countHigher) + " measurements that are larger than the previous measurement")