import sys

line = sys.stdin.readline()
if line[-1] == "\n":
	word = line [:-1]
else:
	word = line

def reverse_rec(word):
	if len(word) == 1:
		print(word)
		return
	else:
		print (word[-1], end="")
		reverse_rec(word[:-1])

reverse_rec(word)