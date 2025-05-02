import sys
a = sys.argv[1]
b = sys.argv[2]
lexicon = open("{}".format(str(a)), "r")
c = lexicon.readline()
word = str(b)

lexlist = []


while c:
    lexlist.append(c.rstrip("\n"))
    c = lexicon.readline()


if word in lexlist:
    print("According to the lexicon, the frequency rank of the word '" + word + "' is", lexlist.index(word)+1)
    letters = set(list(word))
    ordered = sorted(letters)
    print("\n" + word,"contains the letters:" + "\n" + "\t" "-",ordered)
else:
    print("According to the lexicon,", word, "is not in the 4000 most common words in the American English Language")
    letters1 = set(list(word))
    ordered1 = sorted(letters1)
    print("\n"+ word,"contains the letters:" + "\n" + "\t" "-", ordered1)