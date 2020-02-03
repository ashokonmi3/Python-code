# from get_nic import getnic

# getnic.interfaces()

# ======================

# import os
# print(os.getcwd())
# os.chdir('test')
# print(os.getcwd())
# ====================
# import os
# print(os.path.join('/test/', 'myfile'))
# print(os.path.expanduser('~'))
# print(os.path.join(os.path.expanduser('~'),'dir', 'subdir', 'k.py'))

# finding if user is root user
# import os

# uid = os.getuid()

# print( 'Your uid is' +  str(uid)) 
# username = os.system("whoami")
# print( 'Your username is' + str( username) ) 

# if username == 0 :
# 	print ("r00tness!")
# else:
# 	print("Noo! I be a mortal!")
# ========================




# import stat, sys, os, string, commands

# #Getting search pattern from user and assigning it to a list

# try:
#     #run a 'find' command and assign results to a variable
#     pattern = raw_input("Enter the file pattern to search for:\n")
#     commandString = "find " + pattern
#     commandOutput = commands.getoutput(commandString)
#     findResults = string.split(commandOutput, "\n")
#     print(findResults)
#     #output find results, along with permissions
#     print "Files:"
#     print commandOutput
#     print "================================"
#     for file in findResults:
#     	mode=stat.S_IMODE(os.lstat(file)[stat.ST_MODE])
#     	# stat.S_IMODE Return the portion of the files mode that can be set by os.chmod()
#         print(mode)
#         print "\nPermissions for file ", file, ":"
#         for level in "USR", "GRP", "OTH":
#             for perm in "R", "W", "X":
#                 if mode & getattr(stat,"S_I"+perm+level):
#                     print level, " has ", perm, " permission"
#                 else:
#                     print level, " does NOT have ", perm, " permission"
# except:
#     print "There was a problem - check the message above"


# =============================
# import tarfile, sys

# try:
#     #open tarfile
#     tar = tarfile.open(sys.argv[1], "r:tar")

#     #present menu and get selection
#     selection = raw_input("Enter\n\
#     1 to extract a file\n\
#     2 to display information on a file in the archive\n\
#     3 to list all the files in the archive\n\n")

#     #perform actions based on selection above
#     if selection == "1":
#         filename = raw_input("enter the filename to extract:  ")
#         tar.extract(filename)
#     elif selection == "2":
#         filename = raw_input("enter the filename to inspect:  ")
#         for tarinfo in tar:
#             if tarinfo.name == filename:
#                 print "\n\
#                 Filename:\t\t", tarinfo.name, "\n\
#                 Size:\t\t", tarinfo.size, "bytes\n\
                
#     elif selection == "3":
#     	print tar.list(verbose=True)
# except:
#     print "There was a problem running the program"

# ====================================

# import commands, os, string

# program = raw_input("Enter the name of the program to check: ")

# try:
#     #perform a ps command and assign results to a list
#     output = commands.getoutput("ps -f|grep " + program)
#     proginfo = string.split(output)
#     print proginfo

#     #display results
#     print "\n\
#     Full path:\t\t", proginfo[5], "\n\
#     Owner:\t\t\t", proginfo[0], "\n\
#     Process ID:\t\t", proginfo[1], "\n\
#     Parent process ID:\t", proginfo[2], "\n\
#     Time started:\t\t", proginfo[4]
# except:
#     print "There was a problem with the program."
# ===========================
# import pwd

# #initialize counters
# erroruser = []
# errorpass = []

# #get password database
# passwd_db = pwd.getpwall()

# try:
#     #check each user and password for validity
#     for entry in passwd_db:
#         username = entry[0]
#         password = entry [1]
#         if len(username) < 6:
#             erroruser.append(username)
#         if len(password) < 8:
#             errorpass.append(username)

#     #print results to screen
#     print "The following users have an invalid userid (less than six characters):"
#     for item in erroruser:
#         print item
#     print "\nThe following users have invalid password(less than eight characters):"
#     for item in errorpass:
#         print item
# except:
#     print "There was a problem running the script."

# ==============================

# import os
# os.chdir('/')
# import subprocess
# subprocess.call(['ls','-l'])
# ===============

# import subprocess
# output = subprocess.check_output(['ls','-l'])
# print output
# output = subprocess.check_output(['ls','-l'], shell=True)
# print output
# ==================
# import subprocess
# proc = subprocess.Popen(['echo', '"Hello world!"'],stdout=subprocess.PIPE)
# stddata = proc.communicate()
# print stddata
# ===============
# import subprocess
# proc = subprocess.Popen(['echo', '"Hello world!"'],stdout=subprocess.PIPE)
# (stdoutdata, stderrdata) = proc.communicate()
# print(stdoutdata)

# =========================
# import telnetlib
# import getpass
# import sys
# HOST_IP = "your host ip address"
# host_user = input("Enter your telnet username: ")
# password = getpass.getpass()

# t = telnetlib.Telnet(HOST_IP)
# t.read_until(b"Username:")
# t.write(host_user.encode("ascii") + b"\n")
# if password:
# 	t.read_until(b"Password:")
# 	t.write(password.encode("ascii") + b"\n")

# t.write(b"enable\n")
# t.write(b"enter_remote_device_password\n") #password of your remote device
# t.write(b"conf t\n")
# t.write(b"int loop 1\n")
# t.write(b"ip add 10.1.1.1 255.255.255.255\n")
# t.write(b"int loop 2\n")
# t.write(b"ip add 20.2.2.2 255.255.255.255\n")
# t.write(b"end\n")
# t.write(b"exit\n")
# print(t.read_all().decode("ascii") )
# ===========================
# ============================

# import getpass
# import telnetlib

# # HOST = "http://localhost:8000/"
# HOST = "localhost"

# user = raw_input("Enter your remote account: ")
# password = getpass.getpass()

# tn = telnetlib.Telnet(HOST)

# tn.read_until("login: ")
# tn.write(user + "\n")
# if password:
#     tn.read_until("Password: ")
#     tn.write(password + "\n")

# tn.write("ls\n")
# tn.write("exit\n")

# print (tn.read_all())

# ======================
# SSH using paramiko
import paramiko
import time
ip_address = "host_ip_address"
usr = "host_username"
pwd = "host_password"

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(hostname=ip_address,username=usr,password=pwd)

print("SSH connection is successfully established with ", ip_address)

rc = c.invoke_shell()
for n in range (2,6):
	print("Creating VLAN " + str(n))

rc.send("vlan database\n")
rc.send("vlan " + str(n) + "\n")
rc.send("exit\n")
time.sleep(0.5)

time.sleep(1)
output = rc.recv(65535)
print(output)
c.close

