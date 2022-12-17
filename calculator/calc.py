# This program calculates based on user input and selected numbers

def multiply(numbers):
    math = 1
    for number in numbers:
        number = int(number)
        math = number * math
    return f"The answer is: {math}"

def division(numbers):
    math = 1
    for number in numbers:
        number = int(number)
        math = number / math
    return f"The answer is: {math}"

def subtraction(numbers):
    math = 0
    i = 0
    for number in numbers:
        number = int(number)
        # if i not grater than 1 do number - math this is there to prevent the answer from being a negative number
        if i <= 0:
            math = number - math
            i = 1
        else: math = math - number
            
    return f"The answer is: {math}"

def addition(numbers):
    math = 0
    for number in numbers:
        number = int(number)
        math = number + math
    return f"The answer is: {math}"


print("This is a calculator built by Munchnax! This update was made on Dec 16, 2022... Hopefully it works.... ")
print("If you would like to Multiply Please type M:\nIf you would like to Divide Please type D:\nIf you would like to Subtract Please type S:\nIf you would like to do Addition Please type A:\n")

selection = input("Your Response: ")

match selection:
    case "m":
        print(multiply(input("Type in numbers: ").split()))        
    case "d":
        print(division(input("Type in numbers: ").split()))
    case "a":
        print(addition(input("Type in numbers: ").split()))
    case "s":
        print(subtraction(input("Type in numbers: ").split()))
    case _:
        print("Welp, either my code isn't working or you broke it... Goodjob?..!?")

print("Thanks for testing the program, any issues please email me munchnax.jt@gmail.com or just mssg me on github!")
