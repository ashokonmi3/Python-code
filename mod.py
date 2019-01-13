# s = "If Comrade Napoleon says it, it must be right."
# a = [100, 200, 300]
# # 
# def foo(arg):
#     print(f'arg = {arg}')

# class Foo:
#     pass

# def add(x,y):
#    return x + y

# When you run Python interactively the local __name__ variable is assigned a value of __main__. 
# Likewise, when you execute a Python module from the command line, rather than importing it into another module,
# its __name__ attribute is assigned a value of __main__, rather than the actual name of the module.
#  In this way, modules can look at their own __name__ value to determine for themselves how they are being used, 
# whether as support for another program or as the main application executed from the command line. 

# if __name__ == "main": is used to execute some code only if the file was run directly, and not imported.
if __name__ == "__main__":
	print("Module.py is being run directly")
	def apple():
		print ("I AM APPLES!")
	mystuff = {'Subject': "Java!"}
	print (mystuff['Subject'])
	stringModule = "This is inside Module.py"
	print (stringModule)
	print ("success")

else:
	print("Module.py is being imported into another module")
# 	def sqr(n):
# 		print ("success")
# 		return n+1
	mystuff1 = {'Subject': "Scala!"}
	print (mystuff1)
