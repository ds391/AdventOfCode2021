inputs = open("input", "r")
x = 0 #horizontal position
y = 0 #depth
z = 0 #aim

for l in inputs:
	d = l[0]
	v = int(l.rstrip()[-1])
	if d == "f":
		x += v
		y +=(z*v)
	if d == "b":
		x -= v
	if d == "u":
		z -= v
	if d ==  "d":
		z += v

print("After following these instructions, you would have a horizontal position of " + str(x) + " and a depth of " + str(y))
print("(Multiplying these together produces " + str(x*y))