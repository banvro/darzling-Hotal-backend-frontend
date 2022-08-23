from django.urls import path
from ello import views

 

urlpatterns = [
    path("", views.home, name="home.html"),
    path("home", views.home, name="home.html"),
    path("login", views.login_user, name="loginuser"),
    path("users_list/", views.users_list, name="users-list.html"),
    path("user_search", views.user_search, name="user_search.html"),
    path("search", views.search, name='search.html'),


    path("edit_hotal/<int:id>", views.edit_hotal, name='edit_hotal'),
    path("update_hotal/<int:id>", views.update_hotal, name='update_hotal'),
    path("delete_hotal/<int:id>", views.delete_hotal, name='delete_hotal'),


    path('hotal_view/<int:id>', views.hotal_view, name="hotal_view"),

    path('logout', views.logoutuser, name="handleLogout"),
    path("add_hotel", views.add_hotel, name='add-hotel.html'),
    path("hotel_list/", views.hotel_list, name='hotel-list'),
    path("hotel_list_filter/", views.hotel_list_filter, name='hotel_list_filter'),
    path("forgot-password", views.forgot_password, name='forgot-password.html'),



]