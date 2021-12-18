output = open("output", "a")
inputs = open("input", "r")
x = 0
y = 0

for l in inputs:
	d = l.rstrip()[0]
	v = l.rstrip()[-1]
	match d:
		case "f":
			x =+ v
		case "b":
			x =- v
		case "u":
			y =+ v
		case "d":
			y =- v
print("After following these instructions, you would have a horizontal position of " +x+ "and a depth of "+y)