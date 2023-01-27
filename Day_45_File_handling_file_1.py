"""
File Handling:

File: A medium to store the contents permanently on drive
- Each file has a name and its type/extension

Example:
file.py
sample.txt etc.
----------------------------------------------------
- In python, we ahave 2 types which area supported
- 1. txt (default)
- 2. bin (img, audio, video)
-------------------------------------------------

File Operations :
- Create a file
- Open a file
- Write a file
- Read a file
- Close the file
-------------------------------------------

- Create a file :
open() is used in python to create a file(.txt)

- Different modes available in python open() function
=========================================================
 Character              Meaning

 'r'               Open for reading (default)
 'w'               Open for writing, truncating the file first
 'x'               Create a new file, and open it for writing
 'a'               Open for writing, appending to the end of the
                   file if it exists
 'b'               Binary mode
 't'               Text mode(default)
 '+'               Open a disk file for updating (reading and writing)
==========================================================================

- Lets create a.txt file

To create a file
We can use 3 modes:
w: open for writing, truncating the file first
# open(File_Name, mode)
f = open('a.txt', mode='w')
# Truncate means remove old content if any available in already
  present file
# f is now handle for the file a.txt
print(f)
# check different properties of a.txt
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print('Is file closed:', f.closed)
f.close() # it will close the file
print('Is file closed after calling close():', f.closed)
-----------------------------------------------
a : append mode
- It will create a new file if its not present
- and if the file is present with some contents in it
- Then it will add a new contents to the end of the file

Example:
f = open('c.txt', 'a')
# to add a new file only ones to perform write operation
f.write('\nNew contents added\nc.txt is updated')
--------------------------------------------------

x : exclusive mode
- It will create a new file only once to perform write operation
- If the file is already present then it will raise an error.
---------------------------------------
f= open(file='d.txt', mode='x')
# f = open('d.txt', 'x')

- Now you try to open c.txt which is created before c.txt
f = open('c.txt', 'x')
# c.txt is already present, it will give an error
-----------------------------------------------------------
f = open('a.txt', 'w')
f.write('----------------')
====================================================
f = open('aa.txt', 'x')
# you can run above script only once

"""
