import pytest

from django.urls import reverse
from django.test import Client
from .models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profiles_app_index_view():
    client = Client()
    path = reverse('profiles_app:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Profiles</title>"
    assert content.find(expected_content) != -1
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_app_profile_view():
    client = Client()
    user = User.objects.create(username='username_test')
    profile_test = Profile.objects.create(
        user=user,
        favorite_city='favorite_city_test',
    )
    path = reverse('profiles_app:profile',
                   kwargs={'username': profile_test})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>" + str(profile_test) + "</title>"
    assert content.find(expected_content) != -1
    assert response.status_code == 200
