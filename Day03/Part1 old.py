from collections import Counter
file = open("TestData", "r")
inputs = list(file.read().splitlines())
rows = len(inputs)
columns = len(inputs[0])
gamma = ''
epsilon = ''
bit0 = []
bit1 = []
bit2 = []
bit3 = []
bit4 = []
bit5 = []
bit6 = []
bit7 = []
bit8 = []
bit9 = []
bit10 = []
bit11 = []

for x in inputs:
	bit0.append(x[0])
	bit1.append(x[1])
	bit2.append(x[2])
	bit3.append(x[3])
	bit4.append(x[4])
	bit5.append(x[5])
	bit6.append(x[6])
	bit7.append(x[7])
	bit8.append(x[8])
	bit9.append(x[9])
	bit10.append(x[10])
	bit11.append(x[11])
	
gamma = int(str(Counter(bit0).most_common()[0][0])+str(Counter(bit1).most_common()[0][0])+str(Counter(bit2).most_common()[0][0])+str(Counter(bit3).most_common()[0][0])+str(Counter(bit4).most_common()[0][0]+str(Counter(bit5).most_common()[0][0])+str(Counter(bit6).most_common()[0][0]+str(Counter(bit).most_common()[0][0],2)
epsilon = int(str(Counter(bit0).most_common()[-1][0])+str(Counter(bit1).most_common()[-1][0])+str(Counter(bit2).most_common()[-1][0])+str(Counter(bit3).most_common()[-1][0])+str(Counter(bit4).most_common()[-1][0]),2)

print(epsilon*gamma)