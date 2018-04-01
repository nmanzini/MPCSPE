import sys

line = sys.stdin.readline()
first,last = line.split(" ")
last = last[:-1]
length = len(last)
noble = ""
if length == 5:
	length -= 1
while length > 0:
	length -= 1
	noble += last
print (first, noble)