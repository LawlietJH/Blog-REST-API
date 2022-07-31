from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_api import views


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('visits', views.WebsiteVisitCountViewSet)

urlpatterns = [
    path('xyzzy-login-web-page/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
