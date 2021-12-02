import requests

data = {
        'X' : [[3, 22, 1, 0, 7.25, 0, 1, 0, 0, 1]]
        }

response = requests.post('http://localhost:8000/predict', json=data)

print(response)
