import sys
movies_file = sys.argv[1]
ratings_file = sys.argv[2]


a = open("{}".format(movies_file), "r")
b = a.readline()
movieslist = []


c = open("{}".format(ratings_file), "r")
d = c.readline()
filelist = []


while b:
    movieslist += (b.rstrip("\n").split("|"))
    b = a.readline()

while d:
    filelist += (d.rstrip("\n").replace(",", "").split("|"))
    d = c.readline()

seenlist = []
popularlist = []
ratingslist = []
notpopularlist = []
highestratedlist = []
u = []
variation = []

h = 0

#AVERAGE
for i in range(len(filelist)):
    if i % 2 != 0:
        totalmovies = len(movieslist)
        notseen = filelist[i].count('0')
        seen = totalmovies - notseen
        seenlist += [seen]
        notseen = 0
        seen = 0
    else:
        notseen = 0
        seen = 0
averageseen = sum(seenlist)/len(seenlist)

print("The average student watched ", round(averageseen, 2), "movies out of the 100 given in the CPSC 231 class")


#Popular

for k in range(len(filelist)):
    if k % 2 != 0:
        ratingslist += (filelist[k].split("|"))


for m in range(len(movieslist)):
    h = 0
    for v in range(len(ratingslist)):
            if ratingslist[v][m] == "0":
                h += 1  
    f = len(ratingslist) - h
    popularlist += [f]

max1 = max(popularlist)
max_1 = popularlist.index(max1)
popularlist.remove(max1)
max2 = max(popularlist)
max_2 = popularlist.index(max2)
popularlist.remove(max2)
max3 = max(popularlist)
max_3 = popularlist.index(max3)
popularlist.remove(max3)
max4 = max(popularlist)
max_4 = popularlist.index(max4)
popularlist.remove(max4)
max5 = max(popularlist)
max_5 = popularlist.index(max5)
popularlist.remove(max5)


print("The Top Five Most Popular Movies Were :", "\n", "\t", "-", movieslist[max_1],"\n", "\t", "-",  movieslist[max_2],"\n", "\t", "-",  movieslist[max_3],"\n", "\t", "-",  movieslist[max_4],"\n", "\t", "-",  movieslist[max_5])

#Least Popular

for m in range(len(movieslist)):
    h = 0
    for v in range(len(ratingslist)):
            if ratingslist[v][m] == "0":
                h += 1  
    notpopularlist += [h]

min1 = max(notpopularlist)
min_1 = notpopularlist.index(min1)
notpopularlist.remove(min1)
min2 = max(notpopularlist)
min_2 = notpopularlist.index(min2)
notpopularlist.remove(min2)
min3 = max(notpopularlist)
min_3 = notpopularlist.index(min3)
notpopularlist.remove(min3)
min4 = max(notpopularlist)
min_4 = notpopularlist.index(min4)
notpopularlist.remove(min4)
min5 = max(notpopularlist)
min_5 = notpopularlist.index(min5)
notpopularlist.remove(min5)


print("The Top Five Least Popular Movies Were :", "\n", "\t", "-", movieslist[min_1],"\n", "\t", "-",  movieslist[min_2],"\n", "\t", "-",  movieslist[min_3],"\n", "\t", "-",  movieslist[min_4],"\n", "\t", "-",  movieslist[min_5])



#Highest Rated

for m in range(len(movieslist)):
    u = []
    for v in range(len(ratingslist)):
        if ratingslist[v][m] == "1":
            u.append(1)
        elif ratingslist[v][m] == "2":
            u.append(2)
        elif ratingslist[v][m] == "3":
            u.append(3)
        elif ratingslist[v][m] == "4":
            u.append(4)
        elif ratingslist[v][m] == "5":
            u.append(5)
    if len(u) >= 10:
        averageu = sum(u)/len(u)
        highestratedlist.append(averageu)
    else:
        highestratedlist += "NA"

high1 = max(highestratedlist)
high_1 = highestratedlist.index(high1)
highestratedlist.remove(high1)
high2 = max(highestratedlist)
high_2 = highestratedlist.index(high2)
highestratedlist.remove(high2)
high3 = max(highestratedlist)
high_3 = highestratedlist.index(high3)
highestratedlist.remove(high3)
high4 = max(highestratedlist)
high_4 = highestratedlist.index(high4)
highestratedlist.remove(high4)
high5 = max(highestratedlist)
high_5 = highestratedlist.index(high5)
highestratedlist.remove(high5)

print("The Top Five Highest Rated Movies Were :", "\n", "\t", "-", movieslist[high_1],"\n", "\t", "-",  movieslist[high_2],"\n", "\t", "-",  movieslist[high_3],"\n", "\t", "-",  movieslist[high_4],"\n", "\t", "-",  movieslist[high_5])


#Lowest rating

low1 = min(highestratedlist)
low_1 = highestratedlist.index(low1)
highestratedlist.remove(low1)
low2 = min(highestratedlist)
low_2 = highestratedlist.index(low2)
highestratedlist.remove(low2)
low3 = min(highestratedlist)
low_3 = highestratedlist.index(low3)
highestratedlist.remove(low3)
low4 = min(highestratedlist)
low_4 = highestratedlist.index(low4)
highestratedlist.remove(low4)
low5 = min(highestratedlist)
low_5 = highestratedlist.index(low5)
highestratedlist.remove(low5)


print("The Top Five Lowest Rated Movies Were :", "\n", "\t", "-", movieslist[low_1],"\n", "\t", "-",  movieslist[low_2],"\n", "\t", "-",  movieslist[low_3],"\n", "\t", "-",  movieslist[low_4],"\n", "\t", "-",  movieslist[low_5])




#Contentious
highestratedlist = []
for m in range(len(movieslist)):
    u = []
    for v in range(len(ratingslist)):
        if ratingslist[v][m] == "1":
            u.append(1)
        elif ratingslist[v][m] == "2":
            u.append(2)
        elif ratingslist[v][m] == "3":
            u.append(3)
        elif ratingslist[v][m] == "4":
            u.append(4)
        elif ratingslist[v][m] == "5":
            u.append(5)
    if len(u) >= 10:
        averageu = sum(u)/len(u)
        highestratedlist.append(averageu)
    else:
        highestratedlist.append("NA")

for m in range(len(movieslist)):
    u = []
    for v in range(len(ratingslist)):
        if ratingslist[v][m] == "1":
            u.append((1 - highestratedlist[m]) ** 2)
        elif ratingslist[v][m] == "2":
            u.append((2 - highestratedlist[m]) ** 2)
        elif ratingslist[v][m] == "3":
            u.append((3 - highestratedlist[m]) ** 2)
        elif ratingslist[v][m] == "4":
            u.append((4 - highestratedlist[m]) ** 2)
        elif ratingslist[v][m] == "5":
            u.append((5 - highestratedlist[m]) ** 2)
    if len(u) >= 10:
        sumu = sum(u)
        variation.append(((1 /(len(ratingslist)) * sumu)))
    else:
        variation += "NA"



Vari1 = max(variation)
Vari_1 = variation.index(Vari1)
variation.remove(Vari1)
Vari2 = max(variation)
Vari_2 = variation.index(Vari2)
variation.remove(Vari2)
Vari3 = max(variation)
Vari_3 = variation.index(Vari3)
variation.remove(Vari3)
Vari4 = max(variation)
Vari_4 = variation.index(Vari4)
variation.remove(Vari4)
Vari5 = max(variation)
Vari_5 = variation.index(Vari5)
variation.remove(Vari5)

print("The Top Five Highest Contentious Movies Were :", "\n", "\t", "-", movieslist[Vari_1],"\n", "\t", "-",  movieslist[Vari_2],"\n", "\t", "-",  movieslist[Vari_3],"\n", "\t", "-",  movieslist[Vari_4],"\n", "\t", "-",  movieslist[Vari_5])