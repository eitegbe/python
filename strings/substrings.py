class FindSubstring(object):
	def __init__(self):
		pass

	def numberOfoccurences(self, text1, text2):
		length_t1 = len(text1) #record lengths of strings 
		length_t2 = len(text2)
		diff = length_t2 - length_t1 
		count = 0    #initialized variable to keep track of occurences

		for i in range(diff+1):
			for j in range(length_t1):
				if text2[i+j].lower() != text1[j].lower():
					break

			if j == length_t1-1:  #if j matches the length of substring, keeps track of count
				count = count + 1 

		print("Number of occurences of \'{}\', found in \'{}\' is: {}".format(text1, text2, count))


if __name__ == "__main__":
	s = FindSubstring()
	s.numberOfoccurences("abc", "fgfgfzabcgyAbChfy bht ABC")

