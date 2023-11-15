print("Lets start")
"""import requests
url="https://dummyjson.com/products/1"
response = requests.get(url)
if response.status_code == 200:
    print(response.status_code)
    print(response.json().get('id'))
    print(response.json().get('description'))
else:
    print(response.status_code)
    x=1/2
    print(x)"""
    
with open('second_Program.py','r') as file:
	
	for i in range(0,5):

		file_contents = file.readline()

		print(file_contents)

	