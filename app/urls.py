from django.urls import path
from app import views as library_views  # alias



urlpatterns = [

    path('home/', library_views.welcome_page, name="home_page"),
    path('show-books/', library_views.show_all_books, name="show_books"),
    path('show-single-book/<int:bid>/',library_views.show_single_book, name="show_single_book"),
    path('add-book/', library_views.add_single_book, name="add_single_book"),
    path('edit-single-book/<int:bid>/', library_views.edit_single_book, name="edit_single_book"),
    path('delete-single-book/<int:bid>/', library_views.delete_single_book, name="delete_single_book"),
    path('soft_delete-single-book/<int:bid>/', library_views.soft_delete_single_book, name="soft_delete_single_book"),
    path('show-inactive-books/',library_views.show_inactive_books, name="show_inactive_books"),
    path('restore-single-book/<int:bid>', library_views.restore_single_book, name="restore_single_book"),
    path('form-view/', library_views.form_view, name="form_view"),
    path('create-csv/',library_views.create_csv, name="create_csv"),
    path('upload-csv/',library_views.upload_csv, name="upload_csv"),
    path('view-a/',library_views.view_a, name="view_a"),
]