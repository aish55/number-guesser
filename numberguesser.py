import random
topN = int(input("what are the top bands?"))
ran = random.randint(1,topN)
while True:
	  guess  = int(input("Guess"))
	  if guess == ran:
	  	print("yay you won")
	  	# false
	  elif guess > ran:
	  	print("too high")
	  elif guess < ran:
	  	print("too low")
	  else:
	  	print("try again")
