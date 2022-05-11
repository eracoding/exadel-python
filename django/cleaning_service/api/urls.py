from django.urls import path
from . import view

app_name = 'api'

urlpatterns = [
    path('user/list', view.UserListView.as_view(), name='user-list'),
    path('user/detail/<int:pk>', view.UserDetailView.as_view(), name='user-detail'),
    path('user/create', view.UserCreateView.as_view(), name='user-create'),
    path('user/<int:pk>/update', view.UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/delete', view.UserDeleteView.as_view(), name='user-delete'),
]
