from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('xyzzy-admin-web-page/', admin.site.urls),
    path('api/', include('rest_api.urls'))
]
