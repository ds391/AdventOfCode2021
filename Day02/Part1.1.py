output = open("output", "a")
inputs = open("input", "r")
x = 0
y = 0

for l in inputs:
	d = l.rstrip()[0]
	v = int(l.rstrip()[-1])

	if d == "f":
		x =+ v
	elif d == "b":
		x =- v
	elif d == "u":
		y =+ v
	if d ==  "d":
		y =- v
	else:
		print("oops")

print("After following these instructions, you would have a horizontal position of " + str(x) + "and a depth of " + str(y))