from math import floor

input()
array = [int(x) for x in input().split(" ")]
validarray = [x for x in array if x >= 0]
if validarray == []:
	print ("INSUFFICIENT DATA")
else:
	print(floor(sum(validarray)/len(validarray)))