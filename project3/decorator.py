def add_and_double(a,b):
	return (a+b)*2


# def add_and_double_as_float(a,b):
# 	return float(add_and_double(a,b))


#add_and_double = add_and_double_as_float
#result = add_and_double(1,2) # should give us 6.0
# doesn't work this way!
# it's overwritten at this time.


#correct way to do it:


def asFloat(data):
	return float(data)

def wrap(func):
	def wrapper(*args, **kwargs): # accepts any positional and keyword arguments, packs gthem in args/kwargs
		return asFloat(func(*args,**kwargs))
	return wrapper


def increment(a):
	return a+1


result = add_and_double(1,2)

print(result)


def add(a,b):
	return a+b


print(increment(1))