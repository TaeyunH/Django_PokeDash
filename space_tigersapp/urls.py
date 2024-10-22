from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  # Landing page view
    path('home/', views.index, name='index'),  # Homepage view (after login)
    path('new/', views.new, name='new'),  # Demo page view
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Login page view
    path('signup/', views.signup, name='signup'),  # Signup view
    path('logout/', LogoutView.as_view(next_page='landing'), name='logout'),  # Logout view (redirect to landing after logout)
]
