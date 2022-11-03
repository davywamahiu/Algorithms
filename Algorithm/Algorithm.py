#from array import array
#from math import remainder


#dic = {"David", "Charles", "Peter"}
#for x in dic:
#    print(x)


#dic.add("Carol")
#for x in dic:
#    print(x)


#sum = 0
#def addno(arr,target):
#    print("Function starts here")
#    for x in range(0,len(arr) - 2):
#        for i in range(1, len(arr) -1):
#            sum = i+x
#            if sum == target:
#                print("Answer ",sum)
#                return sum


#target = 9
#arr = [ 2, 3, 5, 5, 4, 7, 8]
#ans =addno(arr,target)
#print(ans)

#def reverse(num):
#    print("Reverse has started")
#    ans = ""
#    chungwa = ""
#    r = len(num) -1
#    for x in range(len(num)):
#        if(num[r] == " "):
#            y = len(ans) - 1
#            for i in range(len(ans)):
#                chungwa += ans[y]
#                y -= 1
#            chungwa += " "
#            ans = ""
#        else:
#            ans += num[r]
#        r -= 1
#    y = len(ans) - 1
#    for i in range(len(ans)):
#        chungwa += ans[y]
#        y -= 1
#    return chungwa

#num = "the sky is blue"
#pd = reverse(num)
#print(pd)


#def swapnumber(nums):
#    reminder = nums
#    numb = 0
#    while reminder > 0:
#        reminder = reminder / 10
#        mod = reminder - int(reminder)
#        numb = numb * 10 + mod*10
#        reminder = int(reminder)

#    return int(numb)

#nums = 13
#ans = swapnumber(nums)
#print(ans)

#def palinumb(isbool):
#    num1 = 311
#    reminder = num1
#    numb = 0
#    while reminder > 0:
#        reminder = reminder / 10
#        mod = reminder - int(reminder)
#        numb = numb*10 + mod*10
#        reminder = int(reminder)
#        numb = int(numb)
#        print(numb)
#    if numb == num1:
#        print("I was here")
#        isbool = True
#    return isbool

#isbool = None
#ans1 = palinumb(isbool)
#print(ans1)

#def searchtree(number, targets):
#    right = len(number)
#    left = 0
#    mid  = 0
#    while left < right:
#        mid = (right+left) / 2
#        mid = int(mid)
#        if targets > number[mid-1]:
#            left = mid + 1
#        if targets < number[mid-1]:
#            right = mid - 1
#        if number[mid-1] == targets:
#            return number[mid-1], targets
#    return 0, targets

#number = [ 2, 4, 6, 7, 8, 43, 67, 78, 86, 96, 106 ]
#targets = 67
#tg = searchtree(number, targets)
#print(tg)

#class Node:
#    def __init__(self, dataval=None):
#        self.dataval = dataval
#        self.nextval = None

#class Slinkedlist:
#    def __init__(self):
#        self.headval = None

#    def listprint(self):
#        printval = self.headval
#        while printval is not None:
#            print(printval.dataval)
#            printval = printval.nextval
#    def ATBegning(self, newdata):
#        NewNode = Node(newdata)

#lst = Slinkedlist()
#lst.headval = Node("David")
#l1 = Node("Munene")
#l2 = Node("Peter")
#lst.headval.nextval = l1
#l1.nextval = l2
#lst.ATBegning("Kang'ura")
#lst.listprint()

#from secrets import randbelow


#def rotate(rot):
#    l = len(rot)
#    z = l - 1
#    v = l - 1
#    k = 3
#    print("Am here!!! .Step 1")
#    while k > 0:
#        temp = rot[z]
#        y = v
#        print("Am here!!! .Step 2")
#        while y > 0:
#            rot[y] = rot[y-1]
#            y = y - 1
#            print(rot, rot[y], rot[y-1])
#        rot[0] = temp
#        k = k -1
#        print("Am here!!! .Step 3")
#    print("Am here!!! .Step 4")
#    return rot

#rot = [ 3, 6, 5, 8, 4, 1]
#answ23 = rotate(rot)
#print(answ23)
#import math as m
#def watertank(water):
#    c = len(water) - 1
#    x = 0
#    y = 0
#    y1 = 0
#    y2 = 0
#    x1 = 0
#    count = 0
#    x2 = 0
#    for i in water:
#        r = c
#        while r > 0:
#            if i[0] != 0:
#                x = water[r][0] - i[0]
#                y = min(water[r][1], i[1])
#                sum1 = x*y
#                if sum1 > count:
#                    count = sum1
#                #else:
#                #    print("We are in step 3 x = ", x)
#                #    sum1 = x*i[1]
#                #    if sum1 > count:
#                #        count = sum1
#                #        print("We are in step 4")
#            r -= 1
#    return count

#water = [[0,0],[1,4],[2,3],[3,5],[4,2],[5,5]]
#anw3 = watertank(water)
#print(anw3)



#import string


#def isanumber(strings):
#    r = len(strings) - 1
#    num = ""
#    isbool = None
#    for i in range(0,r):
#        print(strings[i])
#        if strings[i] == "+" or strings[i] == "-" or strings[i] == " ":
#            if strings[i] == "+":
#                num = "+"
#            if strings[i] == "-":
#                num = "-"
#        elif strings[i].isalpha == True:
#            print("Is true")
#            return isbool
#        elif int(strings[i]) >= 0:
#            num += strings[i]
#            isbool = True
#            print("true")
#        else:
#            return isbool
#    return isbool

#strings = " 123b12a67c"
#num = isanumber(strings)
#print(num)


#from pickletools import long1


#def longestsubs(mystring):
#    l = len(mystring)-1
#    ops = ""
#    alg = ""
#    a = ""
#    b = ""
#    for i in range(0,l):
#        a = mystring[i]
#        if len(ops) == 0:
#            ops = a
#        elif ops[0] != a:
#            ops = ""
#        if a == b:
#            ops += a
#            if len(ops) > len(alg):
#                alg = ""
#                alg = ops
#        b = a
#    return alg

#mystring = "aaaabcdddddbcadcba"
#ans = longestsubs(mystring)
#print(ans)


#def longestnonrepeating(lonstring):
#    l = len(lonstring)-1
#    word1 = ""
#    word2 = ""
#    a = ""
#    b = ""
#    for i in range(0,l):
#        a = lonstring[i]
#        word1 += a
#        r = len(word1) - 1
#        for j in range(0,r):
#            if word1[j] != a:
#                if len(word1) > len(word2):
#                    word2 = word1
#                    print("am here 3 "+ word2 + " " + a)
#            elif word1[j] == a:
#                word1 = ""
#                print("am here 4")
#                break
#    return word2

#lonstring = "abcdefgijklmn "
#kilo = longestnonrepeating(lonstring)
#print(kilo)

#from turtle import Screen


class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class LinkList:
    a = 0
    b = 0
    ans = 0
    def __init__(self):
        self.headval = None

    def printists(self):
        val = self.headval
        while val is not None:
            print(val.dataval)
            val = val.nextval
    def addNewStartNode(self, newdat):
        new = Node(newdat)
        new.nextval = self.headval
        self.headval = new
    def addNodeend(self,newdat):
        nod = Node(newdat)
        if self.headval == None:
            self.headval = nod
            return
        lastnode = self.headval
        while lastnode.nextval:
            lastnode = lastnode.nextval

        lastnode.nextval = nod

    def addMiddlenode(self, middle_node, node):
        if middle_node is None:
            print("My ohh my, its null")
            return
        nod = Node(node)
        nod.nextval = middle_node.nextval
        middle_node.nextval = nod

    def removenode(self):
        delval = self.headval
        if delval is None:
            print("Nothing to write")
            return
        rval = delval
        while delval.nextval is not None:
            print(delval.dataval)
            rval = delval.dataval
            delval = delval.nextval



lst = LinkList()
lst.headval = Node("1")
l = Node("+")
l1 = Node(1)
lst.headval.nextval = l
l.nextval = l1
l2 = Node("wambao")
l1.nextval = l2
#lst.printists()
#lst.addNewStartNode("Your Answer is: ")
#lst.printists()
#lst.addNodeend("Last Node Added")
#lst.printists()
lst.addMiddlenode(lst.headval.nextval, "Kang'ura")
lst.printists()
lst.removenode()
lst.printists()



