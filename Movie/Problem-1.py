import sys
b = sys.argv[1]
filmlist = []
movies = open("{}".format(b), "r")
a = movies.readline()
while a:
    filmlist +=(a.rstrip("\n").split("|"))
    a = movies.readline()
movies.close()
choice = []
c = 0
i = 0
m = len(filmlist)



name = input("What is your Name?   ")
print("Please Rate the Following Movies based on how much you enjoyed them using the following scale:")
print("     0 = Never seen it.")
print("     1 = It was terrible!")
print("     2 = I did not like it...")
print("     3 = It was ok.")
print("     4 = I liked it!")
print("     5 = It was awesome!!")
k = input("Are you ready to begin?  ")
if k == "yes":
    for i in range(m):
        print(i+1)
        while c == 0: 
            rating = eval(input(filmlist[i] + "?  "))
            if rating >= 0 and rating <= 5:
                choice +=([rating])
                c += 1
            else:
                print("Invalid Input")

        c = 0
    ratinglist = open("my.ratings.txt", "w")
    ratinglist.write(str(name) + "\n" + str(choice) + "\n")
    ratinglist.close()
    print("Awesome! Saving Ratings to my.ratings.txt")
elif k == "Yes":
    for i in range(m):
        print(i+1)
        while c == 0: 
            rating = eval(input(filmlist[i] + "?  "))
            if rating >= 0 and rating <= 5:
                choice +=([rating])
                c += 1
            else:
                print("Invalid Input")

        c = 0
    ratinglist = open("my.ratings.txt", "w")
    ratinglist.write(str(name) + "\n" + str(choice) + "\n")
    ratinglist.close()
    print("Awesome! Saving Ratings to my.ratings.txt")

else:
    print("Shutting Down Servey...")

                


        







