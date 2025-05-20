import requests
import pprint


params = {'q' : 'html'}
url = 'https://api.github.com/search/repositories'

response = requests.get(url, params=params)

print("Статус-код:", response.status_code)
print("Форматированный ответ JSON:")
pprint.pprint(response.json())






