def begin_story():
	user_response = 0
	print("you have decided to go with daine after school to practice.what do you do next")
	user_response = 	print("go with daine. he says hes going to throw some passes outside. What do you do next?")
	user_response = int(input("1.go to the field\n2.go get some water real quick\n3.tell your parents youll walk home and then go to field"))
	decision1(user_response)
	
def decision1(user_response):
	if user_response == 1:
		print("go to the field. he sees a former friend and tells you he hates him .what do you do next")
		user_response = int(input("1.tell him hes a snake\n2.tell him to just disregard him\n3.tell him lets show him what we got"))
	elif user_response == 2:
		print("get some water real quick. daine runs into a former friend and had something to say to him")
		user_response = int(input("1.	throw some hands\n2.break up the fight
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		
		decision2(user_response)

def decision2(user_response):
	if user_response == 1:
		print("go to the field. he sees a former friend and tells he hates him. What do you do next?")
		user_response = int(input("1.tell him hes a snake\n2.tell him to just disregard him\n3.tell him lets show him what we got"))
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))

def decision3_1(user_response
	print("This would be the story continuing after the user's second response")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))

def decision2_3(user_response):
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision3_1(user_response)
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision3_2(user_response)
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision3_3(user_response)
		
def decision3_1(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_3(user_response)



    
#This runs the game
user_name = input("Enter your name")
begin_story()
