import requests

# response = requests.post(
#     r"http://127.0.0.1:5000/hello/world?name=John&age=20",
#     json={'key_1': 'value_1', 'key_2': 'value_2'},
#     headers={"Content-Type": "application/json"}
# )
# print(response.status_code)
# print(response.json())

# создадим пользователя по api
# response = requests.post(
#     r"http://127.0.0.1:5000/user/",
#     json={'name': 'new1', 'password': 'password1'},
# )
#
# print(response.status_code)
# print(response.json())

# возьмём только что созданного пользователя с помощью get

response = requests.get(
    r'http://127.0.0.1:5000/user/12',
)
print(response.status_code)
print(response.json())

# patch запрос

# response = requests.patch(
#     r'http://127.0.0.1:5000/user/12',
#     json={'name': 'new_name'},
# )
# print(response.status_code)
# print(response.json())
#
# # delete запрос
# response = requests.delete(
#     r'http://127.0.0.1:5000/user/12',
# )
# print(response.status_code)
# print(response.json())


# создадим пользователя по api с коротким паролем
response = requests.post(
    r"http://127.0.0.1:5000/user/",
    json={'name': 'new32151', 'password': '1'},
)

print(response.status_code)
print(response.json())
