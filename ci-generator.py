#First go at a custom compliment/insult generator.
print(\033[29m "Hi This is my new custom affirmation generator" \033[0m )
name = input("What is your name?: ")
print("Hello", name, ", I want to ask you a couple more questions, so you could feel as if this program was made just for you.")
age = input("How old are you? :")
gender = input("What is your gender? :")
pet = input("Whats is your favorite pet? :")
if pet == "dog" or if pet == "Dog" or if pet == "k9":
    print("Awsome!!, i love dogs too")
elif pet == "cat" or if pet == "Cat" or if pet == "feline" or if pet == "pussy" or if pet == "pussycat" or if pet == "pussy cat" or if pet == "floof":
    print("""I used to be a cat person...
             NO MORE!!!""" )
elif pet == "snake" or if pet == "Snake":
    print("My Favorite animal by far!!")
elif pet == "fish" or if pet == "Fish" or if pet == "aquarium" or if pet == "Aquarium":
    print("Got those too :-) ")
elif pet == "hamster" or if pet == "Hamster":
    print("Thats old)
elif pet == "racoon" or if pet == "Racoon":
    print("Ha!! you gotta tell me where to get one!")
else:
    print("""Im not judging...
    Well... maybe i am judging a little bit. """ )
food = input(name, "what is your favorite food?: ")
if food == "pasta" or if food == "Pasta" or if food == "spaghetti":
    print("ciao italia....")
elif food == "pizza" or if food == "Pizza" or if food == "peperoni pizza":
    print("QawaBanga")
else:
    print("Hmm interesting...ill need to try it out next time we meet. ")
print("We are almost finished with the questions", name, "just a little more patience.")
sport = input("What is your Go To sport  activity? :")
if sport == "skydiving" or if sport == "Skydiving" or if sport == "Sky diving" or if sport == "Sky Diving":
    print("Amazing that we have that in common")
elif sport == "mtb" or if sport == "MTB" or if sport == "Mtb" or if sport == "mountain bike" or if sport == "Mountain Bike" or if sport == "Mountain bike":
    print("That is my best therapy!")
elif sport == "Football" or if sport == "football" or if sport == "soccer" or if sport == "Soccer" or if sport == "kickball" or if sport == "Kickball":
    print("How typical...")
elif sport == "Basketball" or if sport == "basketball" or if sport == "basket ball" or if sport == "Basket Ball":
    print("Air jordan or Lebron james?", name, )
else:
    print("Cool...")
partner = input(name, "Whats your partners/Crushes name? :")
if partner == "pamela anderson" or if partner == "Pamela anderson":
    print("Yeah hi.... Tommy")
else:
    print("Thats a lovely name.")
pt = input("What is your favorite passtime activity? which is not sport or any thing todo with your pet.. or food you hungry troll :-)  : ")
drink = input("What is your favorite drink?")
if drink == "beer" or if drink == "Beer":
    print("Chug em' by the gallons....")
elif drink == "whiskey" or if drink == "Whiskey":
    print("How elegant of you")
else:
    print("Mimosa's fo all...")
print("last but not least...")
os = input("What type of OS do you use?, Mac OS, Linux, Windows, Other... :")
if os == "Windows" or if os == "windows" or if os == "ms windows" or if os == "Ms Windows" or if os == "Ms windows":
    print("Im sorry to hear that...", name, )
elif os == "Mac OS" or if os == "Mac os" or if os == "mac os" or if os == "apple" or if os == "Apple":
    print("I see you are a", gender, "  of culture...", name, )
elif os == "linux" or if os == "Linux":
    print("I see we are dealing with a serious", gender, name, )
#  { name, age, gender, food, pet, sport, partner, pt, drink, os} Parameter to referance to.
print("Now we can start to generate some good vibes...")
day = input("What day is it today? :")
if day == "sunday" or if day == "Sunday" or if day == "SUNDAY":
    print(\033[1;33;44m name, "Look at the sky... it is a great day to be a", gender, "look in the mirror for a few seconds.. dont worry you are only", age, "years old.."\033[0m)
    print(\033[1;33;44m "You have plenty of time to spend adoring yourself, you beautiful", age, "years old", gender, " all that", sport, "you do is paying off"\033[0m)
    print(\033[1;33;44m "After the morning", drink, "Kiss", partner, "passionetly on the lips and tell them you love them"\033[0m )
    print()
elif day == "monday" or if day == "Monday" or if day == "MONDAY":
    print(\033[3;34;43m name, day, "is a bitch for most people..., but here in israel it is just another day", food, "might be a good choice for lunch this ", day, "might also be a good day for ", sport, \033[0m )
    print(\033[3;34;43m "You are a really great", gender,"If you have some spare time maybe check for updates on your", os,\033[0m)
elif day == "tuesday" or if day == "Tuesday" or if day == "TUESDAY":
    print(name, )
elif day == "wednesday" or if day == "Wednesday" or if day == "WEDNESDAY":
    print(name, )
elif day == "thursday" or if day == "Thursday" or if day == "THURSDAY":
    print(\033[1;32;46m name, )
elif day == "friday" or if day == "Friday" or if day == "FRIDAY":
    print(name, )
elif day == "saturaday" or if day =="Saturday" or if day =="SATURDAY":
    print(\033[1;32;45m name, "For gods sake it is", day, "i need to rest...go disturb", partner, "or your", pet,\033[0m  )
else:
    print(name, "What planet does this day of the week belong to?")
#  { name, age, gender, food, pet, sport, partner, pt, drink, os} Parameter to referance to.
#TEXT COLOR	CODE	TEXT STYLE	CODE	BACKGROUND COLOR	CODE
Black	30	No effect	0	Black	40
Red	31	Bold	1	Red	41
Green	32	Underline	2	Green	42
Yellow	33	Negative1	3	Yellow	43
Blue	34	Negative2	5	Blue	44
Purple	35			Purple	45
Cyan	36			Cyan	46
White	37			White	47
#put this table here for referance to the colors... 

