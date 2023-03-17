from art import logo
import os

def printing_operations():
  print("+ \n- \n* \n/ ")

def calculation(numb1, numb2, op):
    if op == "+":
        return numb1+numb2
    elif op =="-":
        return numb1-numb2
    elif op == "*":
        return numb1*numb2
    elif op == "/":
        return numb1/numb2

def printing_calculation(numb1, numb2, op):
    result = calculation(numb1,numb2,op)
    print(numb1, op, numb2, "=", result)
    return result

conti = "no" 
result = 0
while conti != "quit":
    if conti == "no":
        os.system('clear')
        print(logo)
        number1  = int(input("What's the first number? "))
    elif conti == "yes":
        number1 = result
    printing_operations()
    operation = input("Pick an operation: ")
    number2 = int(input("What is the next number? "))
    result = printing_calculation(number1, number2, operation)

    
    conti = input("Would you like to continue? Type 'yes' to continure current calculation, type 'no' to start new calcualtion or type 'quit' to exit program ")