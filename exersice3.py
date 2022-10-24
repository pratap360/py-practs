# exerise for print the no of guess
# no of guesses he took to finish
# game over
n=18
number_of_guesses=1
print("Number of guesses is limited only 9 times: ")
while (number_of_guesses<=9):
    guess_number=int(input("Guess the number:\n"))
    if guess_number<18:
        print("You enter the less number please input greater number:\n")
    elif guess_number>18:
        print("You enter the greater number please input lesser number:\n")
    else:
        print("you won the Game\n")
        print(number_of_guesses,"no. of guesses be took to finish.")
        break
    print(9-number_of_guesses,"no. of  guesses left")
    number_of_guesses=number_of_guesses+1
if(number_of_guesses>9):
    print("Game over")
