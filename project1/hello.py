name = input("Please enter your name: ")
yearOfBirth = ""

year = 2016

# short version
while not yearOfBirth.isnumeric() and int(yearOfBirth) > year:
    yearOfBirth = input("Enter the year you were born in: ")

yearOfBirth = int(yearOfBirth)
age = year - yearOfBirth

message = "Hello, %s!\n" % name
message += "You are %i years old" % age

print(message)


# homework: check if you were born in the future. If yes, ask again.
