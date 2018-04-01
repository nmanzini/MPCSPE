import sys

word = sys.stdin.readline()[:-1]

# If s has only one character, then it is always a palindrome.

# If s has two characters, c1c2, then it is a palindrome only if c1=c2.

# If s has more than two characters, we can think of s as c1s′c2, where c1 is the first character in s, c2 is the last character in s, and s′ is the substring between those two characters. s is a palindrome only if s′ is a palindrome and c1=c2.

def palindorme_check(word):
	if len(word) == 1:
		print ("PALINDROME")
		return
	elif len(word) == 2:
		if word[0] == word[1]:
			print ("PALINDROME")
		else:
			print ("NOT PALINDROME")
		return
	elif word[0] == word[-1]:
		palindorme_check(word[1:-1])
		return
	else:
		print ("NOT PALINDROME")
		return


palindorme_check(word)