import sys

matrix = []

X, Y = [int(x) for x in sys.stdin.readline()[:-1].split(" ")]
Xs, Ys = [int(x) for x in sys.stdin.readline()[:-1].split(" ")]
for i in range (X):
	matrix.append( [int(x) for x in sys.stdin.readline()[:-1].split(" ")])
E = 0


while Ys != Y - 1:
	altitude = matrix[Xs][Ys]
	Ys +=1
	
	b = abs(altitude - matrix[Xs ][Ys])
	if Xs == 0:
		a = b
	else:
		a = abs(altitude - matrix[Xs - 1][Ys])
	if Xs == X - 1:
		c = b
	else:
		c = abs(altitude - matrix[Xs + 1][Ys])

	if b <= a and b <= c:
		E += b
	elif a <= b and a <= c:
		E += a;
		Xs -= 1;
	else:
		E += c;
		Xs += 1;

print (Xs, Ys, E)






