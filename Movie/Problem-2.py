import sys
b = sys.argv[2]
c = sys.argv[1]
ratings = open("{}".format(b), "r")
a = ratings.readline()
movie = open("{}".format(c), "r")
d = movie.readline()
ratingslist = []
movies = []
print("Hello", a.rstrip("\n") + "!")


while a:
    ratingslist +=(a.rstrip("\n").lstrip('[').replace(" ", "").rstrip(']').split(","))
    a = ratings.readline()
ratingslist.pop(0)
while d:
    movies +=(d.rstrip("\n").split("|"))
    d = movie.readline()


totalmovies = len(movies)
notseen = ratingslist.count('0')
seen = totalmovies - notseen

print("From the Survey, you have seen", seen, "of the", totalmovies, "movies.")

print("Your Favourite Movies were:")
for i in range(len(ratingslist)):
    if ratingslist[i] == str(5):
        print(" - ", movies[i])




print("Your Least Favourite Movies were:")
for i in range(len(ratingslist)):
    if ratingslist[i] == str(1):
        print(" - ", movies[i])
        

