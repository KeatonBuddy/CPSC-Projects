"""
import sys
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

def square(i):
    #return the square of 1
    answer = i * i
    return answer
print(square(int(a)))

"""

def any(a,b,c):
    if a or b or c:
        return True
    else:
        return False

def all(a,b,c):
    if a and b and c:
        return True
    else:
        return False

print(any(False, True, False))
print(all(True, True, True))