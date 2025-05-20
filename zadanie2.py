import requests
import pprint

url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': '1'}

response = requests.get(url, params=params)

print('Ответ - записи с userId=1:')
pprint.pprint(response.json())

