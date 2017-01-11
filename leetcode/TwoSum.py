class TwoSum(object):
	"""
	    Use two approaches. 
	    1. for loops.
	    2. Using hashmaps
	"""
	def __init__(self):
		pass

	def Forloops(self, a, target):
		if  a is None or len(a)== 0:
			print "Empty List" #proper exception should be raised
			return None

		for i in xrange(len(a)):
			for x in xrange(i+1, len(a)):
				if a[i] + a[x] == target:
					return i, x

	def usingHashMap(self, a, target):
		if  a is None or len(a)== 0:
			print "Empty List" #proper exception should be raised
			return None

		dict = {}
		for i in xrange(len(a)):
			diff = target - a[i]
			if dict.has_key(diff):
				return dict.get(diff), i
			else:
				dict[a[i]] = i

if __name__ == "__main__":
	a = TwoSum()
	print "Result {}".format(a.Forloops([2, 7, 11, 15], 9))
	print "Result {}".format(a.usingHashMap([2, 7, 11, 15], 9))


