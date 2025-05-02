import sys
movies_file = sys.argv[1]
ratings_file = sys.argv[2]
my_file = sys.argv[3]


a = open("{}".format(movies_file), "r")
b = a.readline()
movieslist = []


c = open("{}".format(ratings_file), "r")
d = c.readline()
filelist = []

e = open("{}".format(my_file), "r")
f = e.readline()
mylist = [] 
mynewlist =[]
myfilelist = []
comparelist = []
u = []
z = []
ratingslist = []
newratingslist = []
namelist = []
recommed = []



while b:
    movieslist += (b.rstrip("\n").split("|"))
    b = a.readline()

while d:
    filelist += (d.rstrip("\n").split("|"))
    d = c.readline()

while f:
    myfilelist += (f.rstrip("\n").lstrip('[').replace(",", "").rstrip(']').replace(" ", "").split("|"))
    f = e.readline()

for i in range(len(filelist)):
    if i % 2 != 0:
        ratingslist += (filelist[i].replace(",","").split("|"))

for m in range(len(ratingslist)):
    u = []
    for v in range(len(movieslist)):
        if ratingslist[m][v] == "1":
            u.append(-5)
        elif ratingslist[m][v] == "2":
            u.append(-3)
        elif ratingslist[m][v] == "3":
            u.append(1)
        elif ratingslist[m][v] == "4":
            u.append(3)
        elif ratingslist[m][v] == "5":
            u.append(5)
        elif ratingslist[m][v] == "0":
            u.append(0)
    newratingslist += [u]

for i in range(len(myfilelist)):
    if i % 2 != 0:
        for k in range(len(movieslist)):
            mylist += (myfilelist[i][k].split("|"))

for m in range(len(movieslist)):
    if mylist[m] == "0":
        mynewlist.append(0)
    elif mylist[m] == "1":
        mynewlist.append(-5)
    elif mylist[m] == "2":
        mynewlist.append(-3)
    elif mylist[m] == "3":
        mynewlist.append(1)
    elif mylist[m] == "4":
        mynewlist.append(3)
    elif mylist[m] == "5":
        mynewlist.append(5)





for i in range(len(ratingslist)):
    z = []
    for j in range(len(movieslist)):
        z.append(int(mynewlist[j]) * int(newratingslist[i][j]))
    comparelist.append(sum(z))


me = max(comparelist)
m_e = comparelist.index(me)
comparelist.remove(me)
mostsimilar = max(comparelist)
most_similar = comparelist.index(mostsimilar)

for i in range(len(filelist)):
    if i % 2 == 0:
        namelist += (filelist[i].split("|"))
print("From your ratings of the 100 movies you rated, your results were the most similar to", namelist[most_similar] + "'s .")
print("From your ratings, we think you will also enjoy:")
for i in range(len(movieslist)):
    if mynewlist[i] == 0:
        if newratingslist[most_similar][i] >= 4:
            recommed.append(movieslist[i])
            print("\t", "-" + movieslist[i])


