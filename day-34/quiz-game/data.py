import requests

params = {
    'amount': 10,
    'type': 'boolean'
}

url = 'https://opentdb.com/api.php'

data = requests.get(url, params=params)
data.raise_for_status()
question_data = data.json()['results']
print(question_data)
