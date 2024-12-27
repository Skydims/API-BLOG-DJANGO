from django.urls import path
from .views import post_list, post_create, post_update, post_delete

urlpatterns = [
    path('', post_list, name='post_list'),  # Daftar postingan
    path('create/', post_create, name='post_create'),  # Tambah postingan
    path('<int:pk>/update/', post_update, name='post_update'),  # Update postingan
    path('<int:pk>/delete/', post_delete, name='post_delete'),  # Hapus postingan
]