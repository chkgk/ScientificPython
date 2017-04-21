from nose.tools import *
import random
# today we are implementing a bubble sort and start with the tests


def sort(numbers):
	for i in range(10):
		for j in range(i):
			if numbers[i] < numbers[j]:
				swapIt(numbers, i, j)
			print(numbers, i, j)
	return numbers


	return numbers

def swapIt(myList, i, j):
	myList[i], myList[j] = myList[j], myList[i]
	#pass


def test_sorting():
	"This should sort a list of numbers"
	
	# arrange
	shuffledList = list(range(10))
	random.shuffle(shuffledList)

	# System under test (act)
	shuffledList = sort(shuffledList)
	
	# assert
	assert_equals(shuffledList, list(range(10)))
	

def test_swappint():
	"This should swap two items in a given list"

	# arrange
	myList = [1, 2]

	# system under test
	swapIt(myList, 0, 1)

	# assert
	assert_equals(myList, [2, 1])