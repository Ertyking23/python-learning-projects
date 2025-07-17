operator=input("what operator would you like to choose?(+ for addition and - for subtraction and * for multiplication and / for division) ")
first_number=input("enter first number ")
second_number=input("enter second number ")
if operator=="+":
    print("your number is ",str(float(first_number)+float(second_number)))
elif operator=="-":
    print("your number is ",str(float(first_number)-float(second_number)))
elif operator=="*":
    print("your number is ",str(float(first_number)*float(second_number)))
elif operator=="/":
    print("your number is ",str(float(first_number)//float(second_number)))
else :
    print("the operator you chose is not valid, choose from + , - , * , / ")