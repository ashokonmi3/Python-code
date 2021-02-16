# import sys
# print(" This is commmand line python program execution")
# program_name = sys.argv[0]
# print ("sys.argv is :", sys.argv)
# print ("program name is : ", program_name)
# # ==========================
# import sys
# arguments=[]
# arguments=sys.argv
# # print (l[0])
# arguments = sys.argv[1:]
# print ("arguments are " ,arguments)
# count = len(arguments)
# print ("the number of parameters passed is :",count)
# =========================
# Reverst of string 
# import sys
# s=sys.argv[1]
# print ("Current string is : ", s)
# print ("Reverse of string : " ,s[::-1])
# =========================
# Reverse of list
# import sys
# l=sys.argv[1:]
# print ("Current list  is : ", l)
# print ("Reverse of list : " ,l[::-1])
# ======================

# Pellindrome of string 
import sys

s=sys.argv[1]
if s==s[::-1]:
	print ("pellindrome")
else:
	print ("not pellindrom")
	
# python .\25_CommandlineArg.py kayak.txt asdfadfadasdfasdfasdf asfdasdfad asdfasdfasdf asdfasdf
# fp=open(sys.argv[1],'w')
# for l in sys.argv[2:]:
# 	fp.write(l)

# fp.write(sys.argv[2])
# Assignment :
# Write all the program which we did till now in command line argument.


