# If the community name appears at the start of the person’s name, that person was a princess.

# If the community name appears at the end of the person’s name, that person was a baron.

# If the community name appears in the middle of the person’s name, that person was a priest.

# If the community name does not appear anywhere in the person’s name, that person was considered a commoner in that community

import sys

word = sys.stdin.readline().rstrip('\n')
length = len(word)
num = int(sys.stdin.readline())
name =""
princess = 0
baron = 0
priest = 0
commoner = 0

for i in range(num):
	name = sys.stdin.readline().rstrip('\n')
	if name [:length] == word:
		princess += 1
	elif name [-length:] == word:
		baron += 1
	elif word in name:
		priest += 1
	else:
		commoner += 1

print(princess, "PRINCESS")
print(baron, "BARON")
print(priest, "PRIEST")
print(commoner, "COMMONER")
