import math

def pythagoras(a,b):
	return math.sqrt(a**2+b**2)

a = 3
b = 4

c = pythagoras(a,b)

print("Als een driehoek twee rechte zijdes heeft van lengte ", a, "en", b, "dan heeft de schuine zijde lengte", c)