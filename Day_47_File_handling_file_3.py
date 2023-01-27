"""
# Read operations:

Add contents in killer.txt
f = open('killer.txt', 'a')
f.write('\nNew contents added\n')
f.write('111111111111111111\n')
f.write('222222222222222222\n')
f.write('333333333333333333\n')
f.close()

# if you want to read all contents from killer.txt
g = open('killer.txt', mode='r') # here default mode is read mode
                                 # so if don/t put anything it will
                                 # take read mode bydefault

#print(g.read())

# if you want to read specific blocks from 0th position
#print(g.read(12))
-----------------------------------------------------------------------
readline() : reads line by line
- limit means read specific blocks form 1st line
- finish the first line then go to next line
------------------------------------------------
# default mode is read mode
f = open('killer.txt')

# read line by line contents form a file
print(f.readline())
print(f.readline())
print(f.readline())

op-->
l1

l2

l3


Process finished with exit code 0
=========================================
# readlines(): list of string
- each line is an element of a list
===========================================
d = open('killer.txt')
# read 8th line from killer.txt file : so put the
# index of that line ie index[10]

print(d.readlines()[10])
print(d.readlines())
# nothing left to read now omce you read one time second
# time it wont show anything but an empty list as an output


op-->
3333333333333333333

[]

Process finished with exit code 0
================================================================
Int. Q- What is the difference between read, readline, and readlines?
===============================================
- Can we read from a specific position??
-> Yes. use seek() and tell()
seek(): will bring a cursor to a given position, and
tell(): will tell the current position of the cursor


f = open('killer.txt')
print(f.tell())
print(f.tell())
print(f.seek(12))
#print(f.read())
-------------------------------------------
op->
0
0
12
ll1
ll2
ll3

Process finished with exit code 0
-----------------------------------------------

Q. Read a content form one file and add it to another
  that is read from killer.txt and add it to kill.txt
ans->
f = open('killer.txt')
w = open('kill.txt', 'w')
# first read the text from killer.txt
data = f.read()
# second write to kill.txt
w.write(data)
=================================================
P.S.- Consider you have a file ps.txt , and it contains:
 'hello Abhishek, How are you? I want to connect with you
  please call me on:345348758'

- Now, from above string fetch only the phone number

f = open('ps.txt', 'w')
f.write('hello Abhishek, How are you? I want '
        'to connect with you, please call me on:345348758')
f.close()

g = open('ps.txt')
data = g.read()

print(data.split(':')[-1])

output:

345348758

Process finished with exit code 0
# form above solution only the phone number is fetched
# the rest of the data is not accessed.

# complete the assignment given in c.txt  'Sir google drive file'


"""

