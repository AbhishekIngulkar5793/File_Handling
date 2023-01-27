"""
File Handling:
- Can we create a file on the desktop?
->Yes
-===========================================
f = open(r'C: \vUsers \vabhis\OneDrive\Desktop\Batch 21\Sample_2.txt', 'w')
# Lets perform some write operations in it.
print('the file is writable', f.writable())
f.write('hii the file is created by abhishek\n')
f.write('just to check if the file sample_2 is created or not\n')
f.writelines(['abhishek: 9639', 'killer:5793'])
f.write('wtf')
print('Is my file closed before using f.close() ?', f.closed)
f.close()
print('Is my file closed after using f.close() ?', f.closed)

output:->
the file is writable True
Is my file closed before using f.close() ? False
Is my file closed after using f.close() ? True

Process finished with exit code 0
# above for not getting unicode escape error I/ve changed the
  path, and added v before u and a with / . :)
# The file sample_2 has been created on your machine
  in the batch21 folder and also the  write operations
  also has been processed.
===================================================
f = open('killer.txt', 'w')
print('Is killer.txt is writable ?:', f.writable())
f.write('What/s up? I have tried to create a file in our '
        'File_handling directory\n')
f.write('------------------------------------------\n')
f.write('now its seems that the file has been created\n')
f.write('and whatever m writing have been written.\n')

paragraph = ['1.A\n', '2.B\n', '3.H\n', '4.I\n']
f.writelines(paragraph)
another = ['This para is to check that list of string has '
           'been added to killer.txt\n', 'ive given two different strings here in a list\n']
f.writelines(another)
f.close()
print('Is my file closed after using f.close()?:', f.closed)

output:

Is killer.txt is writable ?: True
Is my file closed after using f.close()?: True

Process finished with exit code 0
# the 'killer.txt' file have been created and the data
  that we have supplied through 'write() and writelines()'
  functions have been successfully added in 'killer.txt'
  file
===========================================================

Int. Q- What is the difference between write() and writelines()?
-->
-In write() function we can supply data only in string format.
 that is, 'string'
-In writelines() function we can supply data in either string
 format or in list of string format.
 that is, ['string1', 'string2',... 'stringN'] or 'string'
-==========================================================
f = open('killer.txt', 'w')
f.writelines(['l1\n', 'l2\n', 'l3\n'])
f.writelines('ll1\nll2\nll3\n')
=======================================================

# append mode:
f = open('killer.txt', 'a')
f.write('\n3333333333333333333\n')
f.close()
k = open('killer.txt', 'a')
k.write('\nssssssssssssssssssss')
======================================
# Exclusive mode:
g = open('abhishek.txt', 'x')
g.write('only one time write operation\n')
g.write('once we run the program and after that if we\n')
g.write('try to write something then it won/t allow\n')
g.write('it will raise and file exists error\n')

op-->
# It will add all the data we  have provided
# once you run the file and try to write it again
# it won/t allow, it will raise an file already exists error
# As it is an exclusive made using 'x' mode that is exclusive
 mode.

"""

