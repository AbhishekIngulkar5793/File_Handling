"""
File Handling:
-----------------------------

- How to deal with an image file

P.S. Read 1.png and write it to 2.png

f = open('pixels-c-674010.jpg', 'r+b')
# r means Read mode + b means Binary mode
# print(f.read())
# It read image in bytes form
data = f.read()

w = open('1.png', 'w+b')
w.write(data)

output:
-1.png file has been created and the data from
 pixels.jpg has been successfully added in it.
================================================
f = open('pixels.jpg', 'rb')
print(f.read())
===============================================

# CSV File Operations :
CSV- Comma Separated Values
- In order to deal with CSV file
  use csv module of python
-----------------------------------------------
import csv
# lets create one csv file
f = open('Sample.csv', 'w')
# default mode is txt mode
# now lets add some contents
f.write('Name,Age,Place\n')
f.write('Abhishek,25,Pune\n')
f.write('Shreyal,22,Washim\n')
--------------------------------------------
- Here it consider all data as plain text
- But if we want to add a data in its original data type
  then use csv module
-------------------------------------------------
import csv
# let/s create one csv file
f = open('Sample.csv', 'w', newline='')
# let/s create a writer object
wr = csv.writer(f)
# use wr to perform write operations
wr.writerow(['Name', 'Age', 'Place'])
wr.writerow(['Abhi', 25, 'Pune'])
wr.writerow(['Shreyal', 22, 'Washim'])
===========================================
# How to Install external packages in current environment
import xlrd
# We can use, settings=>Project interpreter=> + => search and=>install

# OR

# use terminal
# and write: pip install packagename
# pip install packagename=version
# example: pip install pandas=1.5.2
==================================================

Read operations on CSV

f = open('Sample.csv')
# Let/s Create an reader object for handle f
rd = csv.reader(f)
print(rd)
# It returns object reference code
# Typecast the Object
# print(list(rd))
# OR
# Use for loop

for data in rd:
    print(data)

output:
<_csv.reader object at 0x000001B573FB28D0>
['Name', 'Age', 'Place']
['Abhi', '25', 'Pune']
['Shreyal', '22', 'Washim']

Process finished with exit code 0
==================================================


"""
import csv
f = open('n.txt')
