class Furry_friend:
	
	def __init__ (self, arms = 0.0, legs = 0.0, eyes = 0, tail = False, fur = False):
		self.arms = arms
		self.legs = legs
		self.eyes = eyes
		self.tail = tail
		self.fur = fur

	def furry(self):
		if (self.fur != False):
			print(f'My favorite Animal is furry!')
		else:

			print(f'My favorite animal has no fur!')

	def length(self):
		print(f'My favorite animals legs measure {self.legs} inches and their arms are {self.arms} inches!')

	def eye_number(self):
		print(f'My favorite Animal has {self.eyes} eyes!')

	def tail_number(self):
		if (self.tail != False):
			print("My favorite animal has a tail!")
		else:
			print("My favorite animal has no tail!")

def main():
	myFavoriteAnimal = Furry_friend(6.5,6.8,2, True, True)
	print()
	myFavoriteAnimal.furry()
	print()
	myFavoriteAnimal.length()
	print()
	myFavoriteAnimal.eye_number()
	print()
	myFavoriteAnimal.tail_number()
	print()

if __name__ == "__main__":
	main()

