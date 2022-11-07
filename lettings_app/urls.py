from django.urls import path

from .views import letting, index


urlpatterns = [
    path('', index, name='index'),
    path('<int:letting_id>/', letting, name='letting'),
]
