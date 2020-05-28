
import random

#This function generates the number for the game
def get_num():
    num = random.sample("0123456789", 4)
    num = "".join(num)
    return str(num)


#This function takes input from the user and compares it against all possible errors#
def play(game_num):
    guessed = False
    tries = 0
    while not guessed:
        while True:
            player_num = input("Enter Your Number:") #This condition checks whether the number is of 4 digits
            if len(player_num)!= 4:
                print("Enter a 4 digit number")
                continue

            elif not player_num.isdigit():
                print("The input you entered is not a number")

            else:
                x=0
                for i in range(0,4):
                    x = x + player_num.count(player_num[i])

                # This condition checks whether the number has any repititions or not'''
                if(x!=4):
                    print("Enter a number with different digits")
                    continue
                else:
                    break

        bull_count = 0
        cow_count = 0
        game_num = str(game_num)
        player_num = str(player_num)
        for i in range(0, 4):
            for j in range(0, 4):
                if (i == j) and (game_num[i] == player_num[j]):
                    bull_count += 1
                elif (i != j) and (game_num[i] == player_num[j]):
                    cow_count += 1
                else:
                    pass

        if (bull_count == 4):
            guessed = True
            print()
            print("YOU WON! Congratulations!")
            print("You took" ,tries, " tries to complete the game!")
            break

        else:
            print("Bull Count", bull_count)
            print("Cow Count", cow_count)
            guessed = False
            tries+=1


def main(): #This is the main function
    print("------COWS AND BULLS GAME------")
    print()
    print('''RULES:
    1. The number entered must have 4 different digits.
    2. If the position of the digit is the same as the position within the computer generated number, it is counted as bull.
    3. If the position is different it is counted as a cow''')
    print("Have fun!!")
    print()

    game_num = get_num()
    play(game_num)
    print()
    answer = input("Do you wish to play again? Enter (Y/N)").upper()
    while answer == "Y":
        game_num = get_num()
        play(game_num)

if __name__ == "__main__":
    main()