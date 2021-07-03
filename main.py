import requests

print("Hello from Sergei Emelyanov")

result = requests.get('https://playground.learnqa.ru/api/get_text')

print(result.text)



