myBill = float(input("What was your bill? :")) 
percent1 = int(input("How much do you want to tip?values will be calculated in percent :"))
percent = percent1 / 100
tip = percent * myBill
finalBill = myBill + tip
numberOfPeople = int(input("How many people were you? :"))
answer = finalBill / numberOfPeople 
answer = round(answer, 2)
print("You all owe me :", answer)
