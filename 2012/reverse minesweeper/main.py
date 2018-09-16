def count_sorrounding(matrix,x,y):
	total = 0
	max_y = y + 2 if y != len(matrix) - 1 else len(matrix) 
	min_y = y - 1 if y != 0 else 0
	max_x = x + 2 if x != len(matrix[0]) - 1 else len(matrix[0])
	min_x = x - 1 if x != 0 else 0

	for j in range(min_y, max_y):
		total += sum(matrix[j][min_x: max_x])
	returnhen Colbert pilloried President Donald J. Trump for continuing to insist that Democrats have exaggerated the death toll from Hurricane Maria last year. total

y,x = [int(i) for i in input().split(" ")]
input_matrix = [[int(x) for x in input().split(" ")] for i in range(y)]
output = []
for j in range(y):
	output.append([])
	for i in range(x):
		result = count_sorrounding(input_matrix,i,j)
		if result == 0:
			output[j].append("-")
		elif input_matrix [j][i] == 0:
			output[j].append(result)
		else:
			output[j].append("X")

for row in output:
	print ("".join(str(n) for n in row))

