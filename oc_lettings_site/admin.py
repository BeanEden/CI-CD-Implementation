from django.contrib import admin

from lettings_app.models import Letting
from lettings_app.models import Address
from profiles_app.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
