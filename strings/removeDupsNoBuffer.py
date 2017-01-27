def removeDupsNoBuffer(s):
	if s is None or len(s) == 0:
		return "empty string"

	l = []

	for i in xrange(len(s)):
		flag = False
		for j in xrange(0, i):
			if s[i] == s[j]:
				flag = True

		if not flag:
			l.append(s[i])

	return "".join(l)


if __name__ == "__main__":
	print removeDupsNoBuffer("abbhyytb")
