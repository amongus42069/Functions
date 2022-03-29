#Is even function below
x = int(input("put in a number"))
def is_even(x):
    if x % 2 is 0:
        print("true")
    else:
        print("false")

is_even(x)


#Is integer function below
x = float(input("put in a number"))


def is_int(x):
    if x % 1 == 0:
        print("integer")
    else:
        print("not an integer")
        

is_int(x)

#Prints the total sum for each of the digits. ex 1234 would return 10
n = str(input("put your #"))

def ds(n):
    print(sum(int(digit) for digit in str(n)))

if n > '0':
    ds(n)
else:
    print("less than 1")
    
#Put it in factorial form. So each integer below it is multiplied. For ex 5! would be 5*4*3*2*1
import math

n = int(input("put your #"))

def ds(n):
    return math.factorial(n)

print(ds(n))


#Tells if function is prime

x = int(input("put in a noomber"))


def is_prime(x):
    if x %2 == 0 or x %  x-1 == 0:
        return False
        
    else:
        return True
        
    
    
print(is_prime(x))


#Reverses letters

f = str(input("put in letters pwease "))
def reverse(f):
    str = ""
    for x in f:
        str = x + str
    return str
    
print(reverse(f))


#Takes out all vowels

x = str(input("put in phrase "))

def anti(x):
    y = x.replace('a', '')
    z = y.replace('e', '')
    a = z.replace('i', '')
    b = a.replace('o', '')
    c = b.replace('u', '')
    print(c)
    
anti(x)


#Scrabble

x = str(input("put in yo wrd da swabble "))

score = {'a' : 1, 'e' : 1, 'i' : 1, 'l' : 1, 'n' : 1, 'o' : 1, 'r' : 1, 's' : 1, 't' : 1, 'u' : 1, 'd' : 2, 'g' : 2, 'b' : 3, 'c' : 3, 'm' : 3, 'p' : 3, 'f' : 4, 'h' : 4, 'v' : 4, 'w' : 4, 'y' : 4, 'k' : 5, 'j' : 8, 'x' : 8, 'q' : 10, 'z' :10}
         
def swabble(x):
    points = 0
    word = x.lower()
    for x in word:
        if x in score:
            points += score[x]
    word = points
    return word
print(swabble(x))

#Censors word chosen

x = str(input("write in phrase "))

y = str(input("write in censored word in phrase "))

def censor(x):
    for char in x:
        c = x.replace(y, '*'*len(y))
    print(c)
    
censor(x)

#Tells you how long a certain number repeats in python

def count(sequence, item):
    cnt = 0
    for x in sequence:
        if x == item:
            cnt += 1
        
    print(cnt)

count([3, 3, 7, 6], 3)


#Purifies the list

def purfy(lista):
    thelist = []
    for x in lista:
        if x % 2 == 0:
            thelist.append(x)
    return thelist

#Returns product of all numbers in list

def product(Listaa):
    resultimate = 1
    for x in Listaa:
         resultimate = resultimate * x
    return resultimate
#Well.. It removes duplicates
def remove_duplicates(x):
    huh = []
    for i in x:
        if i not in huh:
            huh.append(i)
    return huh

#Hm.. This determines the median

def median(thelist):
    sorted_list = sorted(thelist)
    length = len(sorted_list)
    center = length // 2
    print(sorted_list)
    
    if length == 1:
        return sorted_list[0]

    elif length % 2 == 0:
        return sum(sorted_list[center - 1: center + 1]) / 2.0

    else:
        return sorted_list[center]


    


