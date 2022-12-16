#making a calculator that can recive input and multiply divide or add and subtract

def multiply(numbers):
    math = 1
    for number in numbers:
        number = int(number)
        math = number * math
    return math
print(multiply(input("Type in numbers: ")))


# empty_lst = []
# answer_lst = []
# m = False
# s= False
# d= False
# a= False

# print("This is a basic calculator made by Munchnax, if you would like to Multiply please type M\nIf you would like to Divide please type D",
# "If you would like to Subtract please type S\n If you would like to Add please type A")


# selection = input("Your selection: ")
# result = 1
# match selection:
#     case "M":
#         usernumbers = input("Please enter atleast two numbers") 
#         for i in usernumbers:
#             empty_lst.append()
#             m = True
#     case "m":
#         usernumbers = input("Please enter atleast two numbers") 
#         for i in usernumbers:
#             empty_lst.append(i)
#     case "D":
#             usernumbers = input("Please enter atleast two numbers") 
#             for i in usernumbers:
#                 empty_lst.append(i)
#                 d = True
#     case "S":
#             usernumbers = input("Please enter two atleast numbers")
#             for i in usernumbers:
#                 empty_lst.append(i)
#                 s = True
#     case "A":
#             usernumbers = input("Please enter two atleast numbers") 
#             for i in usernumbers:
#                 empty_lst.append(i)
#                 a = True
#     case _:
#         print("Well please try again later")

# for item in empty_lst:
#     item = float(item)
#     if m == True or d == True:
#         result = 1
#         if m == True: result = item * result
#         else: result = item / result
#     if s == True or a == True:
#         result = 0
#         if a == True: result = item + result
#         else: result = result - item

# answer_lst.append(result)

# print(f"Result: {answer_lst}")