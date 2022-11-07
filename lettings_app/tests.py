import pytest

from django.urls import reverse
from django.test import Client
from.models import Address, Letting


@pytest.mark.django_db
def test_lettings_app_index_view():
    client = Client()
    path = reverse('lettings_app:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Lettings</title>"
    assert content.find(expected_content) != -1
    assert response.status_code == 200


@pytest.mark.django_db
def test_lettings_app_letting_view():
    client = Client()
    address_test = Address.objects.create(
        number=1,
        street='street_test',
        city='city_test',
        state='state_test',
        zip_code=1,
        country_iso_code='country_iso_code_test'
    )
    letting_test = Letting.objects.create(title="Letting_title",
                                          address=address_test)
    path = reverse('lettings_app:letting',
                   kwargs={'letting_id': letting_test.id})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>"+letting_test.title+"</title>"
    assert content.find(expected_content) != -1
    assert response.status_code == 200
