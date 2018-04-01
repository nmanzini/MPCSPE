# If the outcome of round i is heads, then mi+1=mi+bi.

# If the outcome of round i is tails, then mi+1=mi−bi.

# The game ends once all n rounds have been played or if, in any given round i, mi=0 (the player is broke and can’t continue playing).

# If the player lost round i (i.e., the coin flip produced tails), then bi+1=min(2⋅bi,mi+1).

# If the player won round i (i.e., the coin flip produced heads), then bi+1=min(b1,mi+1).

# The first three lines contain the values of m1, b1, and n, respectively. The fourth line contains n integers, each separated by a single space. These integers specify the outcome of the n coin flips in the game: a 1 indicates heads, and a 0 indicates tails.

import sys

mi = int(sys.stdin.readline())
bi = int(sys.stdin.readline())
n = int(sys.stdin.readline())

games = [int(x) for x in sys.stdin.readline().split()]

m = mi
b = bi

for result in games:
	if m == 0:
		break
	if result == 1:
		m = m + b
		b = min(bi ,m)
	else:
		m = m - b
		b = min(2 * b ,m)

if m == 0:
	print ("BROKE")
else:
	print(m)




