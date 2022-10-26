# secret_word="giraffe"
# guess=""
# guess_count=1
# guess_limit=3
# result = False
#
#
# while guess != secret_word and not(result):
#     if guess_count <= guess_limit:
#         guess=input("Enter guess: ")
#         guess_count= guess_count+1
#     else:
#         result = True
# if result:
#     print("You lose")
# else:
#     print("Fine you win!")


secret_word = "bingo"
guess=""

guess_count=1
guess_max=3
out_of_guess = False

while guess != secret_word and not (out_of_guess):
    if guess_count <= guess_max:
        guess = input("Please guess the word: ")
        guess_count+=1
    else:
        out_of_guess=True

if out_of_guess:
    print("You lose!")
else:
    print("Fine you win")