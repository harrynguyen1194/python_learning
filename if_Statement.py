# is_male = True
# is_tall = False
#
# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are male but not tall")
# elif not(is_male) and is_tall:
#     print("You are not male but tall")
# else:
#     print("You are not either male and tall")




# def max_num(num1,num2,num3):
#     if num1>=num2 and num1>=num3:
#         return num1
#     elif num2>=num1 and num2>=num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(3000,40,5000000 ))
#

sun = True
rain = False

if sun:
    print("Bring sunglasses")
elif rain:
    print("Bring umberlla")

#The operation with 2 numbers
num1 = float(input("Enter first num: "))
num2 = float(input("Enter second num: "))
op= input("Enter operation: ")
if op == "+":
    print(num1+num2)
elif op =="-":
    print(num1-num2)
elif op =="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("error")
