import requests

url = r"http://127.0.0.1:8080/user"

response = requests.post(url,
                         json={"name": "user423_now1", "password": "123"}
                         )

print(response.status_code)
print(response.text)

created_now_user_id = 1

response = requests.get(f'{url}/{created_now_user_id}')

print(response.status_code)
print(response.text)

response = requests.patch(f'{url}/{created_now_user_id}',
                          json={"name": "new_name3", "password": "new_password"})


print(response.status_code)
print(response.text)

response = requests.delete(f'{url}/{created_now_user_id}')

print(response.status_code)
print(response.text)
