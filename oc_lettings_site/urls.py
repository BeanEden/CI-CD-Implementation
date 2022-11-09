from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include(('oc_lettings_app.urls', 'oc_lettings_app'), namespace='oc_lettings_app')),
    path('lettings/', include(('lettings_app.urls', 'lettings_app'), namespace='lettings_app')),
    path('profiles/', include(('profiles_app.urls', 'profiles_app'), namespace='profiles_app')),
    path('admin/', admin.site.urls),
]
