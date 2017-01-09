class CountCharacter(object):
	def __init__(self):
		pass

	def countCharacter(self, s):
		if s is None:
			return 
		dict ={}
		for i in s:
			if i in dict:
				count = dict[i] + 1
				dict[i] = count
			else:
				dict[i] = 1

		print(dict)

		for i in dict:
			if dict[i] > 1:
				print("Letter {} appeared {}".format(i, dict[i]))




if __name__=="__main__":
	g = CountCharacter()
	g.countCharacter("Welcomem")
