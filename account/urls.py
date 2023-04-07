from django.urls import path
from .import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.UserListApiView.as_view()),
    path('register/', views.RegistrationView.as_view()),
    path('activate/<uuid:activation_code>/', views.LinkActivationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
