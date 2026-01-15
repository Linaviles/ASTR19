def f(x):
	return (x ** 3) + 8

def main():
	x = 9
	print(f(x))

	if (f(x) > 27):
		print("YAY!")

	else:
		print("NAY :( ")

if __name__ == "__main__":
	main()