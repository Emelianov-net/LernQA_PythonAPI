import requests

print("Hello from Sergei Emelyanov")

result = requests.get('https://playground.learnqa.ru/api/get_text')
print(result.text)

payload = {"name": "user"}
result = requests.get('https://playground.learnqa.ru/api/hello', params=payload)
print(result.text)


