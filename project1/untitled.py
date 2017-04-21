name = input("Please enter your name: ")
yearOfBirth = ""

year = 2016



allOk = False

while not allOk:
	yearOfBirth = input("Enter the year you were born in: ")
	if yearOfBirth.isnumeric():
		yearOfBirth = int(yearOfBirth)
		if yearOfBirth <= year:
			allOk = True

age = year - yearOfBirth

message = "Hello, %s!\n" % name
message += "You are %i years old" % age

print(message)


# homework: check if you were born in the future. If yes, ask again.
