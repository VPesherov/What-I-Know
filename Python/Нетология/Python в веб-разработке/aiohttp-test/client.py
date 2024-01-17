import requests

response = requests.get("http://127.0.0.1:8080/hello/world")
print(response.status_code)
print(response.text)

response = requests.post("http://127.0.0.1:8080/hello/world?name=John&age=20",
                        json={"name": "user_3", "password": "123"},
                        headers={'token': "123"}
                        )

print(response.status_code)
print(response.text)