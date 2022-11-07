from django.contrib import admin
from django.urls import path, include

from oc_lettings_app.views import index


urlpatterns = [
    path('', index, name='index'),
    path('lettings/', include(('lettings_app.urls', 'lettings_app'), namespace='lettings_app')),
    path('profiles/', include(('profiles_app.urls', 'profiles_app'), namespace='profiles_app')),
    path('admin/', admin.site.urls),
]
