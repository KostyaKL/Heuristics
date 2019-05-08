### Tshai Barshevsky 311334544
### Kostya Lokshin 310765821

import random
import string

def exercise1(a, b):
    print("Sum=", a+b)
    print("Sub=", a-b)
    print("Mul=", a*b)
    print("Div=", a/b)
    print("Pow=", pow(a, b))
    print("Mod=", a%b)

def exercise2(a):
    print("Pow=", pow(a,a))

def exercise3(R):
    PAI = 3.14
    print("perimeter=", 2*PAI*R)
    return 2*pow(R, 2)

def exercise4(a, b, c):
    list = [a, b, c]
    print("Max=", max(list))
    print("Min=", min(list))

def exercise5(grade):
    yes = False
    for i in range(0,101):
        if i == grade:
            yes = True
    if yes:
        print("Success")
    else:
        print("Not in range")

def exercise6(list):
    list = [random.randrange(0, 10) for _ in range(10)]
    print(list)

def exercise7(list):
    list = [random.randrange(0, 10) for _ in range(10)]
    list.sort()
    print(list)

def exercise8(list):
    list = [random.choice(string.ascii_letters) for _ in range(10)]
    list.sort()
    return list

def exercise9(list):
    sum = 0
    size = len(list)
    for i in range(0,size):
        sum += list[i]
    print(sum)
    return (sum / size)

def exercise10():
    set = {random.randrange(0, 10) for _ in range(5)}
    print("Before adding:", set)
    x = False
    for i in range(0,2):
        while x == False:
            adding = random.randrange(0, 10)
            if not (adding in set):
                x = True
                set.add(adding)
        x = False
    print("After adding :", set)

def exercise11():
    print("int's functions:", dir(int))
    print("float's function:", dir(float))

def exercise13():
    for i in range(1,101,3):
        print(i)

#exercise1(3,2)
#exercise2(3)
#exercise2(3.4)
#print("area=", exercise3(2))
#exercise4(4,2,3)
#exercise5(100)
#exercise6(list)
#exercise7(list)
#print(exercise8(list))
#print(exercise9([1,2,3,4,5]))
#exercise10()
#exercise11()