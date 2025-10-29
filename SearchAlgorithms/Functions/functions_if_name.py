# file called functions_if_name.py

def my_func(name):
	print(f'Hello, {name} !')

print("Name module functions_if_name", __name__)

if __name__ == "__main__": # test your functions here 
	print("Whatever is in this block only runs when this module is executed directly (python functions_if_name.py)")
	my_func("CSC15 student first")
