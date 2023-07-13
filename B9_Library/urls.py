"""
URL configuration for B9_Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('book/home/', views.welcome_page, name="home_page"),
    # path('book/show-books/', views.show_all_books, name="show_books"),
    # path('book/show-single-book/<int:bid>/',views.show_single_book, name="show_single_book"),
    # path('book/add-book/', views.add_single_book, name="add_single_book"),
    # path('book/edit-single-book/<int:bid>/', views.edit_single_book, name="edit_single_book"),
    # path('book/delete-single-book/<int:bid>/', views.delete_single_book, name="delete_single_book"),
    # path('book/soft_delete-single-book/<int:bid>/', views.soft_delete_single_book, name="soft_delete_single_book"),
    # path('book/show-inactive-books/',views.show_inactive_books, name="show_inactive_books"),
    # path('book/restore-single-book/<int:bid>', views.restore_single_book, name="restore_single_book"),
    # path('book/form-view/', views.form_view, name="form_view"),

    # path('view-a/',views.view_a, name="view_a"),

    path("__debug__/", include("debug_toolbar.urls")),
     # user_app urls

    path('user/', include('user_app.urls')),

    # library urls
    path('book/',include('app.urls')),

    # class_based urls
    path('cbv/', include('cbv_app.urls')),
]




