# FizzBuzz

# Originally a drinking game, count from 1 to 100 one after another. 
# Every time the number is divisible by three, you say fizz. 
# Every number divisible by five is replaced with buzz. 
# If the number is divisible by 3 and 5, you say fizzbuzz, 
# so the progression is:   
# 1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16, and so on 
# Tipp: Find out about the Modulo Operator (%)

# for i in range(1,100):
# 	if i % 3 == 0 and i % 5 == 0:
# 		print("fizzbuzz")
# 	elif i % 3 == 0:
# 		print("fizz")
# 	elif i % 5 == 0:
# 		print("buzz")
# 	else:
# 		print(i)
# print(fizzBuzz2(30))

def rightWord(number):
	if number % 15 == 0:
		return "buzzfizz"

	if number % 5 == 0:
		return "buzz"

	if number % 3 == 0:
		return "fizz"

	return str(number)

def print_result(result):
	# print("\n".join(result))
	for i in result:
		print(i)
		print('-'*len(i))


def main():
	out = [rightWord(number) for number in range(1,100)]
	print_result(out)

if __name__ == "__main__":
	main()