print("Enter Your subjects marks")

#Get users Marks
Maths = int(input("Mathematics score: "))
Physics = int(input("Physics score: "))
Geography = int(input("Geography score: "))
Chemistry = int(input("Chemistry Score: "))
print("\n")
print("Calculating average marks...")
print("\n")

#Calculate only positive & less than 100 marks
if (Maths < 0 or Physics < 0 or Geography < 0 or Chemistry < 0):
    print("Unrecognized marks!")
elif (Maths > 100 or Physics > 100 or Geography > 100 or Chemistry > 100):
    print("Unrecognized marks!")
else:
    average = (Maths + Physics + Geography + Chemistry)/4
    print(f"Average marks is: {average}")

#Generate grade
try:
    if average <= 30:
        print("Your grade is: D")
    elif average <=50:
        print("Your grade is: C")
    elif average <= 70:
        print("Your grade is: B")
    else:
        print("Congrats, your grade is: A")
except NameError:
    print("Check your input marks!")