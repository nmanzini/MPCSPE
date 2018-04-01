
import sys

data = [int(x) for x in sys.stdin.readline().split()]

# print(data)

def clean(data):
	if sum(data) < 30:
		for i in data:
			if i >= 6:
				print("CLEAN")
				return
		print("DO NOT CLEAN")
	else:
		print("CLEAN")


clean(data)