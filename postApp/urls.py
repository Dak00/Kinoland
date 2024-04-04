from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('post/all/', views.allPost, name='allPost'),
    path('post/add/', views.addPost, name='addPost'),
    path('post/view/<int:pk>/', views.postDetail, name='postDetail'),
    path('post/delete/<int:pk>/', views.deletePost, name='deletePost'),
    path('post/edit/<int:pk>/', views.editPost, name='editPost'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

]
