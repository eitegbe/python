def reverseString(s):
	if s is None or len(s) == 0:
		return  #normally throw an exception
	"""s = s.strip()
	r = []*len(s)
	for i in xrange(len(s)-1, -1, -1):
		r.append(s[i])
	print (''.join(r)) """
	s = s.strip().split(" ")
	r = []*len(s)
	for i in xrange(len(s)-1, -1, -1):
		r.append(s[i])
	print ' '.join(r)

if __name__=="__main__":
	reverseString("space before    ")

