inp = [int(n) for n in input().split(" ")]

def gcd (a,b):
	if a == b:
		return (a)
	elif a > b:
		return(gcd (a - b, b))
	else:
		return(gcd(a, b - a))

print(gcd(inp[0],inp[1]))