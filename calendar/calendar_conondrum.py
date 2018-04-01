
import sys

line = sys.stdin.readline()

a,b,c = line.split(" ")

a = int(a)
b = int(b)
c = int(c)

if a > 31:
	print ("Format #3")
elif a > 12 and a <=31:
	if c > 31:
		print("Format #2")
	else:
		print("ambiguous")
else:
	if b >12:
		print("Format #1")
	else:
		print("ambiguous")