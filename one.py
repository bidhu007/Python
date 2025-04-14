#File Name = one.py

def one_func():
	print("I am inside one.py one_func")

def one_func_1():
	print("I am inside one.py one_func_1")

if __name__ == "__main__":
	print("one.py is being called directly")
	one_func()
else:
	print("one.py is being imported")