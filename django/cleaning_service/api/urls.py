from django.urls import path
from . import view

app_name = 'api'

urlpatterns = [
    path('user/', view.UserListView.as_view()),
    path('user/create', view.UserCreateView.as_view()),
    path('user/<int:pk>', view.UserUpdateView.as_view()),
    path('user/<int:pk>/delete', view.UserDeleteView.as_view()),

    path('review/', view.ReviewListView.as_view()),
    path('review/create', view.ReviewCreateView.as_view()),
    path('review/<int:pk>', view.ReviewUpdateView.as_view()),
    path('review/<int:pk>/delete', view.ReviewDeleteView.as_view()),

    path('request/', view.RequestListView.as_view()),
    path('request/create', view.RequestCreateView.as_view()),
    path('request/<int:pk>', view.RequestUpdateView.as_view()),
    path('request/<int:pk>/delete', view.RequestDeleteView.as_view()),

    path('service/', view.ServiceListView.as_view()),
    path('service/create', view.ServiceCreateView.as_view()),
    path('service/<int:pk>', view.ServiceUpdateView.as_view()),
    path('service/<int:pk>/delete', view.ServiceDeleteView.as_view()),
]

# path('user/list', view.UserListView.as_view(), name='user-list'),
# path('user/detail/<int:pk>', view.UserDetailView.as_view(), name='user-detail'),
# path('user/create', view.UserCreateView.as_view(), name='user-create'),
# path('user/<int:pk>/update', view.UserUpdateView.as_view(), name='user-update'),
# path('user/<int:pk>/delete', view.UserDeleteView.as_view(), name='user-delete'),
# path('review/list', view.ReviewListView.as_view(), name='review-list'),
# path('service/list', view.ServiceListView.as_view(), name='service-list'),
# path('request/list', view.RequestListView.as_view(), name='request-list'),

