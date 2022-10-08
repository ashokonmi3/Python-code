import json

#Parse JSON (Convert from JSON to Python)
# json.loads() method can parse a json string and the result will be a Python dictionary.
# #
# # JSON string
# employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
#
# Convert string to Python dict
# employee_dict = json.loads(employee)
# print(employee_dict)
# print(type(employee_dict))
# print("\n")
# print(employee_dict["id"])
# print(employee_dict["name"])
# # #send dump
# # # # Convert Python dict to JSON
# json_object = json.dumps(employee_dict, indent=4)
# print(json_object)
# print(type(json_object))

# ===============================
# Python program showing
# use of json package

# import json
#
# # {key:value mapping}
# a = {"name": "John",
#      "age": 31,
#      "Salary": 25000}
#
# # conversion to JSON done by dumps() function
# b = json.dumps(a)
#
# # printing the output
# print(b)
# ===================
# Python program showing that
# json support different primitive
# types
# #
# import json
#
# # list conversion to Array
# print(json.dumps(['Welcome', "to", "GeeksforGeeks"]))
#
# # tuple conversion to Array
# print(json.dumps(("Welcome", "to", "GeeksforGeeks")))
#
# # string conversion to String
# print(json.dumps("Hi"))
#
# # int conversion to Number
# print(json.dumps(123))
#
# # float conversion to Number
# print(json.dumps(23.572))
#
# # Boolean conversion to their respective values
# print(json.dumps(True))
# print(json.dumps(False))
#
# # None value to null
# print(json.dumps(None))
# #
# # Python object	       JSON object
# # dict	               object
# # list, tuple	           array
# # str	                   string
# # int, long, float	   numbers
# # True	               true
# # False	               false
# # None 	               null
# =======================
# indention
# Data to be written
# dictionary = {
# 	"id": "04",
# 	"name": "sunil",
# 	"depatment": "HR"
# }
#
# # Serializing json
# json_object = json.dumps(dictionary, indent=4)
# print(json_object)
#
# # =======================
'''dump function turns it to json and then streams it on into a file, 
meanwhile dumps turns it into str.
'''
# var = {
#     "Subjects": {
#         "Maths": 85,
#         "Physics": 90
#     }
# }
# with open("Sample.json", "w") as p:
#     json.dump(var, p)
# ======================
# Deserializing JSON :
# The Deserialization is the opposite of Serialization, i.e. conversion of JSON object into their respective Python objects.
# The load() method is used for it. If you have used Json data from another program or obtained as a string format of Json,
# then it can easily be deserialized with load(), which is usually used to load from string, otherwise,
# the root object is in list or dict.
# with open("Sample.json", "r") as read_it:
# 	data = json.load(read_it)
# print(data)
# print(type(data))
# ================

# json_var ="""
# {
#     "Country": {
#         "name": "INDIA",
#         "Languages_spoken": [
#             {
#                 "names": ["Hindi", "English", "Bengali", "Telugu"]
#             }
#         ]
#     }
# }
# """
# var = json.loads(json_var)
# print(var)
#=========================
# import requests
# import json
#
# res = requests.get("https://jsonplaceholder.typicode.com/todos")
# var = json.loads(res.text)
# print(var)

# =========================

# Updating a json string.
# Python program to update
# JSON
#
import json

# JSON data:
x = '{ "organization":"GeeksForGeeks","city": "Noida","country": "India"}'

# python object to be appended
y = {"pin": 110096}

# parsing JSON string:
z = json.loads(x)

# appending the data
z.update(y)

# the result is a JSON string:
print(json.dumps(z))
