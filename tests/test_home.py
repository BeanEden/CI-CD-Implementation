import pytest

from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_profiles_app_index_view():
    client = Client()
    path = reverse('profiles_app:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Holiday Homes</title>"
    assert content.find(expected_content) != -1
    assert response.status_code == 200
