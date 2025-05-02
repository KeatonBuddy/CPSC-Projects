import Hangman
import stddraw
import sys
import random
a = sys.argv[1]
lexicon = open("{}".format(str(a)), "r")
c = lexicon.readline()
lexlist = []
longlexlist = []
randomletterlist = []
guesses = 8
guessed = []
hangmanword = []
g = []

while c:
    lexlist.append(c.rstrip("\n"))
    c = lexicon.readline()

for i in range(len(lexlist)):
    if len(lexlist[i]) >= 4:
        longlexlist.append(lexlist[i])
randomword = random.choice(longlexlist)

for i in range(len(randomword)):
    randomletterlist.append(randomword[i])



Hangman.setscreensize(-10,-10,10,10)
Hangman.title(0,9,"Jokerman",25,stddraw.DARK_GRAY,"WELCOME TO HANGMAN!")
Hangman.drawHangman(-3, -3, 3, 7,5)
Hangman.wordBlanks(len(randomword),-8)
Hangman.subtitles(-5, 6, "Letters Guessed Wrong", 0, -6, "Secret Word:")



while guesses > 0:
    print("The Secret Word Looks like This:")
    if g == []:
        print(("_ "*len(randomletterlist)))
    else:
        print(g)
    stddraw.show(500)
    print("You have", guesses, "guesses left!")
    d = input("What is your guess? ")


    if d not in guessed:
        guessed.append(d)

        if d in randomletterlist:
            print("\n"+ "You've Guessed the Letters: ", ",".join(guessed))

            for i in range(len(randomletterlist)):
                for j in range(len(guessed)):
                    if randomletterlist[i] == guessed[j]:
                        hangmanword.append(randomletterlist[i])
                        Hangman.fillBlanks(randomletterlist[i], i, len(randomletterlist), -7)
                        break
            
                if randomletterlist[i] != guessed[j]:
                    hangmanword.append("_")
            g = ("{} "*len(hangmanword)).format(*hangmanword)
            
        else:
            print("\n"+ "You've Guessed the Letters: ", ",".join(guessed))
            print("Sorry there is no '"+ d + "' in the secret word")
            guesses = guesses -1
            Hangman.wrongLetter(d, guesses, 5)
            Hangman.HangmanMan(3,5,guesses)
                
    else:
        print("\n"+ "You guessed '",d,"' already!!")
        
    
    if g:
        if "_" not in g:
            break
    hangmanword = []

    stddraw.show(500)


if guesses == 0:
    print(g)
    print("\n"+ "YOU RAN OUT OF GUESSES!!")
    

if guesses != 0:
    print(g)
    print("\n"+ "YOU GUESSED THE SECRET WORD!")

print("\n"+ "The secret word was: '"+randomword+"'" )

stddraw.show()