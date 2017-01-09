class NumberOfWords(object):

	def __init__(self):
		pass

	def countwords(self, s):
		if s is None:
			return 0
		count = 0
		prev = ' '
		for i in xrange(len(s)):
			a = s[i]
			if a != prev and prev == ' ':
				count += 1
			prev = a

		return count


if __name__ == '__main__':
	s = NumberOfWords()
	print(s.countwords("   yt  jf fj "))