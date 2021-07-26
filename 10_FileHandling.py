#!/usr/bin/env python
# coding: utf-8

# Now, coming to Python – There are 2 types of files mainly:
# 
# Binary
# 
# Text
# 
# Binary files are categorized as the generic 0’s and 1’s in Python too.
# 
# A binary file is any type of file that is not a text file. Because of their nature, binary files can only be processed by an application that knows or understand the file’s structure. In other words, they must be applications that can read and interpret binary.
# 
# Text files are structured as a sequence of lines, where each line includes a sequence of characters. This is what you know as code or syntax. Each line is terminated with a special character, called the EOL or End of Line character.

# At its core, a file is a contiguous set of bytes used to store data. This data is organized in a specific format and can be anything as simple as a text file or as complicated as a program executable. In the end, these byte files are then translated into binary 1 and 0 for easier processing by the computer.
# Files on most modern file systems are composed of three main parts:
# 
# Header: metadata about the contents of the file (file name, size, type, and so on)
# <br>Data: contents of the file as written by the creator or editor
# <br>End of file (EOF): special character that indicates the end of the file

# In[ ]:





# * 'r' - reading mode. The default. It allows you only to read the file, not to modify it. When using this mode the
# file must exist. DEFAULT MODE
# * 'w' - writing mode. It will create a new file if it does not exist, otherwise will erase the file and allow you to
# write to it.
# * 'a' - append mode. It will write data to the end of the file. It does not erase the file, and the file must exist for
# this mode.
# * 'rb' - reading mode in binary. This is similar to r except that the reading is forced in binary mode. This is
# also a default choice.
# * 'r+' - reading mode plus writing mode at the same time. This allows you to read and write into files at the
# same time without having to use r and w.
# * 'rb+' - reading and writing mode in binary. The same as r+ except the data is in binary
# * 'wb' - writing mode in binary. The same as w except the data is in binary.
# * 'w+' - writing and reading mode. The exact same as r+ but if the file does not exist, a new one is made.
# Otherwise, the file is overwritten.
# * 'wb+' - writing and reading mode in binary mode. The same as w+ but the data is in binary.
# * 'ab' - appending in binary mode. Similar to a except that the data is in binary.
# * 'a+' - appending and reading mode. Similar to w+ as it will create a new file if the file does not exist.
# Otherwise, the file pointer is at the end of the file if it exists.
# * 'ab+' - appending and reading mode in binary. The same as a+ except that the data is in binary.
<filePointerVariable>=open(<fileName>,<mode>)
# In[ ]:


fp=open("output.txt",'r')


# In[ ]:


type(fp)


# In[ ]:


fp


# In[ ]:


fp.close()
# There are limits on the number of files you can have open - typically something like 512-4096.
# If you neglect to close your files you'll eventually get to the point where you cannot open new 
# file descriptors (files, sockets, etc)


# In[ ]:


fp=open("output.txt")
fp.close()


# One must keep in mind that the mode argument is not mandatory. If not passed, then Python will assume it to be “ r ” by default.

# ### Reading file as a string

# In[ ]:


fp=open("output.txt",'r')


# In[ ]:


dir(fp)
# help(open)


# In[ ]:


fp=open("output.txt",'r')
s=fp.read()
print(s)
fp.close()
# s=fp.read()


# In[ ]:


fp=open("output.txt",'r')
s=fp.read(25)
print(s)
fp.close()


# ### Reading file line by line
# 

# In[ ]:


for i in "python":
    print (i)


# In[ ]:


l=["java","python","scala"]
for i in l:
    print (i)


# In[ ]:


d={"sub1":"java","sub2":"python","sub3":"scala"}
for i in d:
    print (i)


# In[ ]:


d={"sub1":"java","sub2":"python","sub3":"scala"}
for i in d:
    print (d[i],i)


# In[ ]:


fp= open('output.txt', 'r')
for i in fp:
    print(i)


# In[ ]:


fp=open("output.txt",'r')


# In[ ]:


print(fp.readline())
print( "i am after readlne")
print(" Python file handling")
print(" Opening a file in read mode")
l=["java","python","scala"]
for i in l:
    print (i)


# In[ ]:


print(fp.readline())


# In[ ]:


fp.readline()


# In[ ]:


fp.readline()


# In[ ]:


fp.readline()


# In[ ]:


fp.close()
help(fp)


# In[ ]:


fp=open("output.txt",'r')
fp.close()
print(fp)
print(fp.read())


# In[ ]:


with open('output.txt', 'r') as fp:     #fp=open("output.txt",'r')
    for i in fp:
        print(i)
print("after file closing ")
print(fp.read())


# In[ ]:


print("hello")
print("world")
print("\n")
print("python")


# In[ ]:


input_file = open("hello.txt", "r")


# ### Reading file as a LIST

# In[ ]:


fp=open("output.txt",'r')


# In[ ]:


a=fp.readlines()# read()-- string , readline()-- one line at a time
a


# In[ ]:


a[2]


# In[ ]:


print(a[0:2])
print(a[-1])


# In[ ]:


fp.close()


# In[ ]:


print("hello")
print("\n")
print("print")


# #### Writing data to a file

# In[ ]:


fp=open("output1.txt", 'w')


# In[ ]:


fp.write("this is for my test string\n")
fp.close()


# In[ ]:


fp=open("output1.txt", 'w')
a="this is for file operation write operation"
fp.write(a)
line2 = "the emblem of our land for write operation.\n"
fp.write(line2)
fp.write("  this is for my test string\n")
fp.close()


# In[ ]:


output_file = open("output1.txt", "w")
lines_to_write = [
"This is my file.\n",
"There are many like it,\n",
"but this one is mine.\n"]
output_file.writelines(lines_to_write)
output_file.close()


# #### Append mode

# In[ ]:


output_file = open("output1.txt", "a")
l=["This is to append","\nThis will be last line in the file"]
output_file.writelines(l)
output_file.close()
# output_file


# In[ ]:


# fh = open("output12.txt", "a")
# fh.write("\nHello World again to append2")
fp.close()


# In[ ]:





# In[ ]:


fc=open("output12.txt", 'r+')
i=fc.tell()
print ("Initial file pointer position",i)
fc.seek(20)
i=fc.tell()
print (f"After seek 20 file pointer position {i}")
fc.close()


# In[ ]:


fc=open("output12.txt", 'r+')
i=fc.tell()
print ("Initial file pointer position",i)
fc.seek(4)
fc.write("abcd")
i=fc.tell()
print ("After seek file pointer position",i)
fc.close()


# In[ ]:





# In[ ]:


import os ,sys
fc=open("output12.txt", 'rb+')
fc.seek(4)
# i=fc.tell()
# print (i)
# fc.write(" Ending ")
# fh.close()
fc.seek(5,0)
print(fc.tell())
fc.seek(5,1)
print(fc.tell())
# fc.seek(-2,1)

fc.seek(-2,2)

print(fc.tell())
# help(fc)

seek(self, target, whence=0, /)
 |      Change stream position.
 |      
 |      Change the stream position to the given byte offset. The offset is
 |      interpreted relative to the position indicated by whence.  Values
 |      for whence are:
 |      
 |      * 0 -- start of stream (the default); offset should be zero or positive
 |      * 1 -- current stream position; offset may be negative
 |      * 2 -- end of stream; offset is usually negative
 |      
 |      Return the new absolute position.
# In[ ]:


in_file=open('output.txt', 'r')
out_file=open('output_file.txt', 'w')
with open('output.txt', 'r') as in_file, open('output_file.txt', 'w') as out_file:
    for line in in_file:
        out_file.write(line)

print("this is after autometic close ")


# In[ ]:


with open('somefile.txt', 'w+') as f:
    # Note that f has now been truncated to 0 bytes, so you'll only
    # be able to read data that you write after this point
    f.write('somedata\n')
    f.seek(0)  # Important: return to the top of the file before reading, otherwise you'll just read an empty string
    data = f.read() # Returns 'somedata\n'
    print(data)
print("file closed")


# The Python docs say that w+ will "overwrite the existing file if the file exists". So as soon as you open a file with w+, it is now an empty file: it contains 0 bytes. If it used to contain data, that data has been truncated — cut off and thrown away — and now the file size is 0 bytes, so you can't read any of the data that existed before you opened the file with w+. If you actually wanted to read the previous data and add to it, you should use r+ instead of w+.

# In[ ]:


import shutil
shutil.copyfile(src, dst)


# In[ ]:


import shutil
source='//192.168.1.2/Daily Reports'
destination='D:\\Reports\\Today'
shutil.copytree(source, destination)


# # Assignment
# * find a string "Python" in a file
# * till now whatever programs we did , do with file handling
# * With open is used for what?
# * Write string, list, tuple, set and dictionary data to file
# * Prompt for a number N and file F, and display the first N lines of F.
# * Write a "pager" program. Your solution should prompt for a filename, and display the text file 25 lines at a time, pausing each time to ask the user to "press a key to continue."
# * Create a crude and elementary text file editor. Your solution is menudriven, with the following options: a. create file [prompt for filename and any number of lines of input], b. display file [dump its contents to the screen], c. save file, and d. quit.
# * Write a program to compare two text files. If they are different, give the line and column numbers in the files where the first difference occurs.
# * https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
# * Find the errors in log file
# * You have 2 log files , merge them and sort by time , first charcets are time
# 

# 1. Write a Python program to read an entire text file. 
# 
# 2. Write a Python program to read first n lines of a file. 
# 
# 3. Write a Python program to append text to a file and display the text. 
# 
# 4. Write a Python program to read last n lines of a file. 
# 
# 5. Write a Python program to read a file line by line and store it into a list.  
# 
# 6. Write a Python program to read a file line by line store it into a variable.  
# 
# 7. Write a Python program to read a file line by line store it into an array. 
# 
# 8. Write a python program to find the longest words. 
# 
# 9. Write a Python program to count the number of lines in a text file. 
# 
# 10. Write a Python program to count the frequency of words in a file. 
# 
# 11. Write a Python program to get the file size of a plain file. 
# 
# 12. Write a Python program to write a list to a file. 
# 
# 13. Write a Python program to copy the contents of a file to another file . 
# 
# 14. Write a Python program to combine each line from first file with the corresponding line in second file. 
# 
# 15. Write a Python program to read a random line from a file. 
# 
# 16. Write a Python program to assess if a file is closed or not. 
# 
# 17. Write a Python program to remove newline characters from a file. 
# 
# 

# In[ ]:


1.
def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('test.txt')

2.
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('test.txt',2)

3.
def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Java Exercises")
        txt = open(fname)
        print(txt.read())
file_read('abc.txt')

4.
import sys
import os
def file_read_from_tail(fname,lines):
        bufsize = 8192
        fsize = os.stat(fname).st_size
        iter = 0
        with open(fname) as f:
                if bufsize > fsize:
                        bufsize = fsize-1
                        data = []
                        while True:
                                iter +=1
                                f.seek(fsize-bufsize*iter)
                                data.extend(f.readlines())
                                if len(data) >= lines or f.tell() == 0:
                                        print(''.join(data[-lines:]))
                                        break

file_read_from_tail('test.txt',2)

5.
def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                content_list = f.readlines()
                print(content_list)

file_read(\'test.txt\')

6.
def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')

7.

def file_read(fname):
        content_array = []
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line)
                print(content_array)

file_read('test.txt')

8.
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))

9.
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("test.txt"))

10.
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))

11.
def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size in bytes of a plain file: ",file_size("test.txt"))

12.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())

13.
from shutil import copyfile
copyfile('test.py', 'abc.py')

14.
with open('abc.txt') as fh1, open('test.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)
		

15.
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('test.txt'))

16.
f = open('abc.txt','r')
print(f.closed)
f.close()
print(f.closed)

17.
def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

print(remove_newlines("test.txt"))


# ### Exercise

# Read in the raw text file poem.txt and display each line by looping over them individually, then close the file

# 

# In[ ]:


input_file = open("C:/test/useless text files/hello.txt", "r")
import os
path = "C:/Real Python/python-basics-exercises"
os.mkdir(os.path.join(path, "My Directory"))

