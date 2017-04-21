def reverseList(liste):
	return [liste[1], liste[0]]


myList = [3,4]
umgekehrteListe = reverseList(myList)
print(umgekehrteListe)


def test_reverseList():
	myList = [3,4]
	assert(reverseList(myList), [4,3])