from django.contrib import admin

from .models import Download
from .models import User

admin.site.register(Download)
admin.site.register(User)