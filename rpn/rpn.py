import sys

items = sys.stdin.readline()[:-1].split(" ")

operators = ["+", "*", "and", "or", "=="]
booleans = ["false", "true"]
result = 0

def rpn(items):
	stack = []
	for i in items:
		# print ("stack", stack)
		if i in operators:
			if len(stack) < 2:
				return "SYNTAX ERROR"
			else:
				a = stack.pop()
				b = stack.pop()
				if type(a) != type(b):
					return "TYPE ERROR"
				elif type(a) == bool and i != "and" and i != "or":
					return "TYPE ERROR"
				elif type(a) == int and (i == "and" or i == "or"):
					return "TYPE ERROR"
				else:
					if i == "+":
						result = a + b
					elif i == "*":
						result = a * b
					elif i == "==":
						result = a == b
					elif i == "and":
						result = a and b
					elif i == "or":
						result = a or b
					stack.append(result)
		elif i in booleans:
			if i == "true":
				stack.append(True)
			if i == "false":
				stack.append(False)
		else:
			stack.append(int(i))
	if len(stack) != 1:
		return "SYNTAX ERROR"
	else:
		result = stack[0]
		if type(result) == bool:
			if result:
				return "true"
			else:
				return "false" 
		else:
			return result

print(rpn(items))