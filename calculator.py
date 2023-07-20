#addition

a = float(input("Enter the 1st value = "))
b = float(input("Enter the 2nd value = "))
choice = input("Enter the operator + - * / : ")
if choice == "+":
    sum = a + b
    print("The sum is ",sum)

elif choice == "-":
    sub = a - b
    print("The sub is " ,sub)

elif choice == "*":
    mutiple = a * b
    print("The mutiple is " ,mutiple)

elif choice == "/":
    div = a / b
    print("The div is " ,div)

else:
    print("Invaild choice")

# = is used for input of the value
# == is used for comparsion
#elif is used for if the codition is true still it will check the all the statemens