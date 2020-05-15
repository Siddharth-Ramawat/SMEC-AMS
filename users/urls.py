from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('view_user/<int:id>', views.view_profile, name='user_profile'),
    path('update_password',views.update_password,name='update_password')
]