def hangman():
    global win,loose
    print("Welcome to the Hangman\n The rules are suuuuuuper complex \n .....Just kidding \n The 'Grammar Nazi' backstage thinks of a word and you have to guess it alphabet by alphabet or else there will be CONSEQUENCES!\n Dont worry though, you have 5 lives to get it right\n The Dashes represent the number of alphabets a word contains\n Enjoy!!")
    print()
    secret=['bulb', 'offset', 'referee', 'method', 'cheat', 'paradox', 'recommendation', 'enlarge', 'jelly', 'revise', 'year', 'emergency', 'abundant', 'pile', 'joy']
    word=r.choice(secret)
    guesses=""
    lives=5
    while lives>0:
        missing=0
        for i in word:
            if i in guesses:
                print(i,end="")
            else:
                print("- ",end="")
                missing+=10
        if missing==0:
            print("\nYou Win!!!")
            win+=1
            break
        guess=input("\nGuess an Alphabet\n")
        guesses+=guess
        if guess not in word:
            lives-=1
            print(f"Nope.... \nTry again \nYou have {lives} lives remaining")
            if lives==4:
                print("Dont forget the Consequences!!!")
                print()
            if lives==3:
                print("|\n|\n|\n|\n|\n|")
                print()
            if lives==2:
                print("__")
                print("|\n|\n|\n|\n|\n|")
                print()
            if lives==1:
                print("__")
                print("|    |")
                print("|\n|\n|\n|\n|")
                print()
            if lives==0:
                print("__")
                print("|    |")
                print("|    O")
                print("|   /|\\")
                print("|   / \\")
                print("|_")
                print("\\___\\")
                print()
                print(f"\nYou loose!!\nThe word was {word}")
                loose+=1
