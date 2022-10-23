print("Wellcome to this website, please provide your information bellow")
name = input("What is your name: ")
print("Hello " + name)
sex = input("What is your gender (Male or Female): ")
print("Your gender is: " +sex)
dob = input("What is your date of birth: ")
age = 2022 - int(dob)
print("You are: " + str(age))
weight = float(input("What is your weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == 'K':
    coverted = weight
    print("Your weigh in Kg is: " +str(coverted))
elif unit.upper()=='L':
    coverted = weight* 2.24
    print("Your weight in L is: " +str(coverted))
