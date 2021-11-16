
import requests
params = {'id': 'c', 'temperature':'v','humidity':'s'}
response = requests.get('https://flask-innovation-project-1.pranavchinni.repl.co/',params=params)
print(response.text)
