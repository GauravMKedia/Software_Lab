from collections import defaultdict

j1,j2=4,3
check =defaultdict(lambda: False)
queue = []
count = 1

def btoaa(a,b):
    if a+b>4:
        return 4
    else:
        return a+b

def btoab(a,b):
    if a+b>4:
        x=b-(4-a)
        return x
    else:
        return 0


def atoba(a,b):
    if a+b>3:
        x=a-(3-b)
        return x
    else:
        return 0


def atobb(a,b):
    if a+b>3:
        return 3
    else:
        return a+b

def repeate_check(temp,a,b):
    if temp[0] == a and temp[1] == b:
        return 0
    else:
        return 1

def solve(a,b):
    global count
    flag = True
    x = 0
    y = 0
    while flag:
        if len(queue) == 0:
            if a == 2:
                return 1
        #elif queue[0][0] == 4:
        #    return 1
        if len(queue) == 0:
            temp = [a, b]
            #print("Temp is ")
            #print(temp)
        else:
            temp = queue.pop(0)
        x = temp[0]
        y = temp[1]
        temp = [0, y]
        if repeate_check(temp, x, y) == 1:
            print(f"\n{count}")
            count = count+1
            print(temp)
            queue.append(temp)
            if temp[0] == 2:
                return 1
        temp = [x, 0]
        if repeate_check(temp, x, y) == 1:
            print(f"\n{count}")
            count = count + 1
            queue.append(temp)
            print(temp)
            if temp[0] == 2:
                return 1
        temp = [4, y]
        if repeate_check(temp, x, y) == 1:
            print(f"\n{count}")
            count = count + 1
            queue.append(temp)
            print(temp)
            if temp[0] == 2:
                return 1
        temp = [x, 3]
        if repeate_check(temp, x, y) == 1:
            print(f"\n{count}")
            count = count + 1
            queue.append(temp)
            print(temp)
            if temp[0] == 2:
                return 1
        temp = [btoaa(a, b), btoab(a, b)]
        if repeate_check(temp, x, y) == 1:
            print(f"\n{count}")
            count = count + 1
            queue.append(temp)
            print(temp)
            if temp[0] == 2:
                return 1
        temp = [atoba(a, b), atobb(a, b)]
        if repeate_check(temp, x, y) == 1:
            print(f"\n{count}")
            count = count + 1
            queue.append(temp)
            print(temp)
            if temp[0] == 2:
                return 1



print("Water Jug Problem :")
print("Enter Initial value of Jugs : ")
print("Jug 1 :")
a=int(input())
print("Jug 2 :")
b=int(input())
print("The solution is :")
solve(a,b)




