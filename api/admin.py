from django.contrib import admin
from .models import UTMParameter

# Register your models here.
admin.site.register(UTMParameter)

# Since User model will be automatically taken by default even if we are not created for any purpose
# User model registration is not required on admin
