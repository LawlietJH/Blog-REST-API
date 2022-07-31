from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('xyzzy-admin-web-page/', admin.site.urls),
    path('api/', include('rest_api.urls'))
] + staticfiles_urlpatterns()
