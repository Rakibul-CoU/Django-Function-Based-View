from django.urls import path

from api.views import create_view, delete_view, detail_view, list_view, update_view

urlpatterns = [
    path('create-view/', create_view, name="create-view"),
    path('list-view/', list_view, name="list-view"),
    path('detail-view/<int:id>/', detail_view, name="detail-view"),
    path('update-view/<int:id>/', update_view, name="update-view"),
    path('delete-view/<int:id>/', delete_view, name="delete-view"),
]