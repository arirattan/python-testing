name = input("HI.., Lets start with your name please. :")
if name == "ari":
  print("Welcome back sir...")

elif name == "dosh":
    print("Holla Carter como estass?")
elif name == "dudu":
    print("Hi man nice to see you again.")
elif name == "sissi":
    print("Ti voglio tanto bene.")

else:
 print("Hi", name,"""Nice to know you, I am goint to ask you a few questions.
       please DO NOT use capital letters...
       Check that your Caps Lock is not ON.
       Sit back and try to enjoy yourself.""")
print()
print(name)
print("Did you have a good or bad nights sleep?")
night = input(":")
if night == ("good","great","wonderful",):
    print("Thats great news")
if night == ("bad", "no"):
    print("Im sorry to hear that, did you try to dissconnect from all your tech 2 hour before you went to bed?")
    tech = input(":")
    if tech == ("yes","sure", "of course", "yeah", "y" ):
        print("Well you should try some yoga in my opinion")
    if tech == ("no", "nop", "not a chance", "not", "n"):
        print("I strongly suggest you dissconnect from all your tech devices 2 hours before you go to sleep")
    else:
        print("Dont start getting funny here!")

    
else:
    print("Thats odd..")
print()
print("""Lets see how well you ate this past day..
      Knowing myself and how difficult it is to maintain a regular and healthy diet, I realised i have to force myself to eat sometimes, due to lack of hunger.""", name,)
print("Do you think your diet is stable?, can you maintain a 3 meal regime?")
meal = input("How many meals do you eat a day? :")
if meal == "1":
    print("Thats not enough", name, "try harder...")
elif meal == "2":
    print("2 meals is a start", name, " lets try to shove at least one more meal in that piehole")
elif meal == "3":
    print("Well done ", name,)
elif meal > "3":
    print("better slow down fat ass, we are not trying to build you a dad Bod")
else:
    print("""Ahhhh, i think we need to start talking about your mental health before we address yourr diet,
         I suggest you ask yourself what is stopping you from feeling hungry.
         maybe even go to a therapist, there is no shame in that, I go regularly.""")
print()
print("Now that we got your", meal, "meals out of the way", name,)
print("I think we can start to see a correlation from the little data we gathered about you, your", night, "night sleep directly reflects on your hunger levels and vice versa.")
print("""Balance is the most important thing you should strive to achieve.
      It is not an easy task""", name, """but i am sure you can Crush It!
      Meditation, Yoga, Self reflection all could help you in your journey""", name, """towards balance""")
print("""Do you pratice:


     \033[31m 
      1.) yoga
      2.) meditation
      3.) self reflection       \033[0m  """) 
practice = input("I practice :")
if practice == ("yoga"):
       print("Thats wonderful!")
elif practice == ("meditation"):
        print("Great")
elif practice == ("self reflection"):
        print("Now thats very good, but i would reccomend adding another dimension to that", name, ", But keep up the good work.")
else:
        print("Im sorry we dont recognise the input you provided as a valid relaxation method", name,
         "please provide a valid parameter")
        input = ("I practice :")
print()
print()
print("Lets dive into more personal questions...")
print(name)
angry = input("Do you get angry easily?:")
if angry == "yes":
     print("Well why dont you keep on eating only", meal, "'s a day, see if that calms you down")
elif angry == "no":
    print("I bet that the fact you had a ", night, "night sleep contributes to your calm.")
    print("Why do you keep messing wth me?")
    answer = input("Why do you keep messing wth me? :")
    if answer == "why not":
        print("Well i think i want you to leave..")
    if answer == "because im a smartass":
        print("thats not very nice is it?")
        answer2 = input("are you here just to test my patience? :")
        if answer2 == "no":
            print("thank you for conferming that.")
        elif answer2 == "yes":
            print("well fuck off then")
        elif answer2 == "why not":
            print("Well go home then...")
    else:    
        print("because you keep on fucking about and making me write more and more nested if's....")
        answer3 = input("and its starting to look really complicated :")
        if answer3 == "i dont care":
            print("you are very rude")
        elif answer3 == "i dont understand":
            print("well try harder")
        elif answer3 == "its not complicated at all":
            print("well what do you mean not complicated?")
            answer4 = input("wait i get it, i just need to practice more and more :")
            if answer4 == "yes":
                print("oh i knew that..")
            elif answer4 == "practice practice practice":
                print("ok ok ok ") 
                answer5 =input("i want to congratulate you for reaching this far. any last words? : ")
                if answer5 =="bye":
                    print("bye")
                elif answer5 == "ciao":
                    print("ciao")
                elif answer5 == "no last words":
                    print("well no last words from me either...")
                    answer6 = input("bye:")
                    if answer6 =="bye":
                        print("BYE!!!!!!!")
                    elif answer6 == "??" :
                        print("FAREWELL")
                    else:
                        print("well that brings us to the end of this questioneer...")
                    print("""Its been a pleasure coding this and learning python,
                          next program will be better""")
