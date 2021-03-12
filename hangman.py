import random
import string
def hangman():
    word = random.choice(["pugger", "littlepugger", "tiger", "holy", "bite", "shadow", "puppy", "howl"])
    turns = 10
    guessmade = ''

    while len(word)>0:
        main = ""

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word: ", main)
        guess = input("Enter a letter: ")

        if guess in string.ascii_lowercase:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input("Enter a letter: ")
        if guess not in word:
            turns -= 1
            if turns == 9:
                print("9 turns left")
                print("------------")
            if turns == 8:
                print("8 turns left")
                print("------------")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("------------")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("------------")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("------------")
                print("     O      ")
                print("     |      ")
                print("    / \     ")

            if turns == 4:
                print("4 turns left")
                print("------------")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")

            if turns == 3:
                print("3 turns left")
                print("------------")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")

            if turns == 2:
                print("2 turns left")
                print("------------")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")

            if turns == 1:
                print("1 turn left")
                print("------------")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            
            if turns == 0:
                print("1 turn left")
                print("------------")
                print("     O_|   ")
                print("    /|\     ")
                print("    / \     ")
                print("You lose")
                break
            
                        
name = input("Enter your name: ")
print("Welcome", name ,"let's play")
print(" ")
print("Try to guess the word in less than 10 tries")
hangman()
