from django.contrib import admin
from rest_api import models


admin.site.register(models.UserProfile)
admin.site.register(models.WebsiteVisitCount)
