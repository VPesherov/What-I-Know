# то что мы хотим достать
'''
<strong class="text-underline"><span class="table-ip4-home"> 111.111.111.111</span></strong>

'''

from bs4 import BeautifulSoup
import requests

# отправляем http запрос
response = requests.get('https://www.iplocation.net/')

# выкачиваем html с помощью атрибута text
html_data = response.text

# создаём экземпляр класса
# первым параметром передаём наш html
# вторым наш парсер
# парсер мы установим pip install lxml
soup = BeautifulSoup(html_data, features='lxml')

# поиск нашего тэга с нужным классом
span_tag = soup.find(name='span', class_='table-ip4-home')
#посмотрим что тут лежит
print(span_tag)
# с помощью атрибута text - получим наше содержимое
ip_addr = span_tag.text

# выводим и обработаем с помощью strip, чтоб убрать лишнее
print(ip_addr.strip())


