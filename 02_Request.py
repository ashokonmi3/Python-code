'''GET	 method is used to retrieve information from the given server using a given URI.
POST	POST request method requests that a web server accepts the data enclosed in the body of the request message,
most likely for storing it
PUT	The PUT method requests that the enclosed entity be stored under the supplied URI.
If the URI refers to an already existing resource, it is modified and if the URI does not point to an existing resource, then the server can create the resource with that URI.
DELETE	The DELETE method deletes the specified resource
HEAD	The HEAD method asks for a response identical to that of a GET request, but without the response body.
PATCH	It is used for modify capabilities. The PATCH request only needs to contain
the changes to the resource, not the complete resource
'''
# # import requests module
# import requests
# # #
# # # # Making a get request
# response = requests.get('https://api.github.com/')
# #
# # # print request object
# print(response.url)
# #
# # # Status code 200 indicates that request was made successfully.
# print(response.status_code)
# # # .content gives you access to the raw bytes of the response payload
# print(response.content)
# #
# # # response.text print the string format
# print(response.text)
# #
# # # The response headers can give you useful information, such as the content type of the response payload and a time limit on how long to cache the response
# print(response.headers)
# #
# # # headers is a dictionary type
# print(response.headers['content-type'])
# ===============================
# importing the requests library
# import requests
#
# # # api-endpoint
# URL = "http://maps.googleapis.com/maps/api/geocode/json"
#
# # location given here
# location = "delhi technological university"
#
# # defining a params dict for the parameters to be sent to the API
# PARAMS = {'address':location}
#
# # sending get request and saving the response as response object
# r = requests.get(url = URL, params = PARAMS)
#
# # extracting data in json format
# data = r.json()
# print(data)
#
# # extracting latitude, longitude and formatted address
# # of the first matching location
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']
#
# # printing the output
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
# 	%(latitude, longitude,formatted_address))
# ========================
# import requests
# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
# )
#
# # Inspect some attributes of the `requests` repository
# print(response.url)
# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Repository name: {repository["name"]}')
# print(f'Repository description: {repository["description"]}')  #
# ===================
# import requests
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.status_code)
# print(r.url)# URL is encoded correctly
# ==================
# import requests
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
#
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url)
# ==============
# HEADERS
# import requests
#
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
#
# r = requests.get(url, headers=headers)
# ========================
# POST Request
# import requests
#
# r = requests.post('https://httpbin.org/post', data = {'key':'value'})
# print(r.status_code)
# =====================
# import requests
#
# payload = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.post("https://httpbin.org/post", data=payload)
# print(r.text)
# =====================
# import requests
# payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
# r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
# payload_dict = {'key1': ['value1', 'value2']}
# r2 = requests.post('https://httpbin.org/post', data=payload_dict)
# print(r1.text)
# ================
# import json
# import requests
#
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
#
# r = requests.post(url, data=json.dumps(payload))
# ==============
# url = 'https://httpbin.org/post'
# files = {'file': open('report.xls', 'rb')}
#
# r = requests.post(url, files=files)
# print(r.text)
# ======================
# importing the requests library
# import requests
#
# # defining the api-endpoint
# API_ENDPOINT = "http://pastebin.com/api/api_post.php"
#
# # your API key here
# API_KEY = "XXXXXXXXXXXXXXXXX"
#
# # your source code here
# source_code = '''
# print("Hello, world!")
# a = 1
# b = 2
# print(a + b)
# '''
#
# # data to be sent to api
# data = {'api_dev_key':API_KEY,
# 		'api_option':'paste',
# 		'api_paste_code':source_code,
# 		'api_paste_format':'python'}
#
# # sending post request and saving response as response object
# r = requests.post(url = API_ENDPOINT, data = data)
#
# # extracting response text
# pastebin_url = r.text
# print("The pastebin URL is:%s"%pastebin_url)
# ================================
# response.raise_for_status()
# If you invoke .raise_for_status(), an HTTPError will be raised for certain status codes.
# If the status code indicates a successful request,
# the program will proceed without that exception being raised.

# import requests
# from requests.exceptions import HTTPError
#
# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#
#         # If the response was successful, no Exception will be raised
#         response.raise_for_status()#404, 502
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')
#     except Exception as err:
#         print(f'Other error occurred: {err}')
#     else:
#         print('Success!')
# ==============
# from getpass import getpass
# import requests
# requests.get('https://api.github.com/user', auth=('username', getpass()))
# ================
import requests

# requests.get('https://api.github.com', timeout=1)
# requests.get('https://api.github.com', timeout=3.05)
# ============
# import requests
# from requests.exceptions import Timeout
#
# try:
#     response = requests.get('https://api.github.com', timeout=1)
# except Timeout:
#     print('The request timed out')
# else:
#     print('The request did not time out')
 # ====================
# requests.put('https# requests.post('https://httpbin.org/post', data={'key':'value'})://httpbin.org/put', data={'key':'value'})
# requests.delete('https://httpbin.org/delete')
# requests.head('https://httpbin.org/get')
# requests.patch('https://httpbin.org/patch', data={'key':'value'})
# requests.options('https://httpbin.org/get')

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(arr)
#     arr.sort()
#     print(arr[len(arr)-2])