from django.urls import path
from .views import LandingPageView, UserRegisterView, UsersLogoutView, UsersLoginView, ProfileView, ContactView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('logout/', UsersLogoutView.as_view(), name='logout'),
    path('login/', UsersLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('profile/', ProfileView.as_view(), name='profile')
]