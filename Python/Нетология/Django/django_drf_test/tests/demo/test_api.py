import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from demo.models import Message


@pytest.mark.django_db
def test_api():
    # Arrange - подготовка данных
    client = APIClient()
    User.objects.create_user('admin')
    Message.objects.create(user_id=1, text='test')
    # Act - тестируемый функционал
    response = client.get('/messages/')
    # Assert - проверка
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['text'] == 'test'

# def test_api2():
#     assert 2 == 2
