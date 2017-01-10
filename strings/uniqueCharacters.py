def uniqueCharacter(s):
	if s is None or len(s)==0:
		return
	dict = {}
	for i in s:
		if i in dict:
			dict[i] += 1
		else:
			dict[i] = 1

	for i in dict:
		if dict[i] > 1:
			print("Characters: {} and count {}".format(i, dict[i]))

if __name__ == "__main__":
	uniqueCharacter("Madam")
	uniqueCharacter("madam")