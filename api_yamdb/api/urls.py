from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register(r'users', views.UsersViewSet, basename='users')
v1_router.register(r'categories', views.CategoryViewSet, basename='category')

urlpatterns = [
    path('v1/auth/signup/', views.SignupAPIView.as_view(), name='signup'),
    path('v1/auth/token/', views.GetTokenAPIView.as_view(), name='tokens'),
    path('v1/', include(v1_router.urls), name='api'),
]
