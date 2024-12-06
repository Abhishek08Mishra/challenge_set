# 1. Numbers and Floats Write a Python function that takes two numbers (integers or floats) as input and returns: ● Their sum ● Their difference ● Their product ● Their division (handle the case where division by zero might occur).

print("\nCalculator")
print(
    "\nWhat type of calculations do you want to perform ? \n\nselect an option from the bellow ; \n\n 1.) Addition \n 2.) Difference \n 3.) Multiplication \n 4.) Division \n 5.) Exit"
)

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multi(num1,num2):
    return num1 * num2

def divi(num1,num2):
    if num2 == 0:
        return "you can't divide by zero"
    else:
        return num1 / num2

while True:
    choice=int(input("\nEnter your choice between 1 and 5 : "))

    if choice not in (1,2,3,4,5,):
        print("Invalid input , please enter a number between 1 and 5")
        continue

    if choice == 5 :
        print("Exiting the calculator")
        break

    num1=int(input("Enter your first number : "))
    num2=int(input("Enter your second number : "))

    if choice == 1:
        print(f"sum of {num1} and {num2} is {add(num1,num2)}")

    elif choice == 2:
        print(f"Difference of {num1} and {num2} is {sub(num1,num2)}")

    elif choice == 3:
        print(f"product of {num1} and {num2} is {multi(num1,num2)}")

    elif choice == 4:
        print(f"Division of {num1} and { num2} is {divi(num1,num2)}")

    next_calc=input("Do you want to continue or exit, type yes for continue and no for exiting from the calculator! : ").lower().strip()

    if next_calc == "yes":
        continue
    
    else:
        print("Exiting the calculator")
        print("Thank you for using calculator! \n Have a good day!!!")
        break