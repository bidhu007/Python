#File Name = two.py
import one


print("I am inside two.py indent-0")

one.one_func()

if __name__ == "__main__":
	print("two.py is being called directly")
else:
	print("two.py is being imported")