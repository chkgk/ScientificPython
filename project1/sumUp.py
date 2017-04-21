def sumUp(flatList, summe = 0):
	if not flatList:
		return summe
	else:
		return sumUp(flatList[:-1], summe+flatList[-1])

# one liner:
def sumUpInOneLine(flatList, summe = 0):
		return summe if not flatList else sumUpInOneLine(flatList[:-1], summe+flatList[-1])



myList = [1, 2, 3, 4, 5, 6]
print("normal: ", sumUp(myList))

print("one-liner: ", sumUpInOneLine(myList));
