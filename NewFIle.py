# Welcome message and age verification
print("Welcome to your Kids Kalculator")
age = int(input("How old are you? "))
# Begin the calculations
def main():
    first_number = int(input("Enter your first number: "))
    operation = input("Enter (+, -, *, /): ")
    second_number = int(input("Enter your second number: "))
# Perform the calculation based on the user's input (under 8)
    if age < 8:
        if operation == "+":
          print("Ka-Chow your answer is " + str(first_number + second_number))
        elif operation == "-":
          print("To infinity... and BEYOND, your answer is " + str(first_number - second_number))
        elif operation == "*":
          print("Theres a Snake in my Boot, your answer is " + str(first_number * second_number))
        elif operation == "/":
            if second_number == 0:
              print("Sorry not this time partner, that can't be divided by 0")
            else:
              print("Ka-Chow your answer is " + str(first_number / second_number))
          # Repeat a calcuation based on the user's input 
        repeat = input("Would you like to do another calculation? (yes/no): ")
        if repeat.lower() == "yes":
          main()
        else:
          print("So long, partner.Thank you for using Kids Kalculator")
        exit
#Perform the calculation based on the user's input (8 and over)       
    if age >= 8:
        if operation == "+":
          print("Hulk smash, your answer is " + str(first_number + second_number))
        elif operation == "-":
          print("Iron Man repulsor blast, your answer is " + str(first_number - second_number))
        elif operation == "*":
          print("Avengers assemble, your answer is "+ str(first_number * second_number))
        elif operation == "/":
              if second_number == 0:
                print("It is inevitable, you can't divide by 0")
              else:
                print("Thor's lightning strike, your answer is "+ str(first_number / second_number))
# Repeat a calcuation based on the user's input  
        repeat = input("Would you like to do another calculation? (yes/no): ")
        if repeat.lower() == "yes":
          main()
        else:
          print("Thank you for using Kids Kalculator, I am Iron Man.")
        exit
main()
