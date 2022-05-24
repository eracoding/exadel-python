from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import view

user_list = view.UserViewSet.as_view({
    'get': 'list'
})

user_create = view.UserViewSet.as_view({
    'post': 'create'
})

user_retrieve = view.UserViewSet.as_view({
    'get': 'retrieve'
})

user_delete = view.UserViewSet.as_view({
    'delete': 'destroy'
})

service_list = view.ServiceViewSet.as_view({
    'get': 'list'
})

service_create = view.ServiceViewSet.as_view({
    'post': 'create'
})

service_retrieve = view.ServiceViewSet.as_view({
    'get': 'retrieve'
})

service_delete = view.ServiceViewSet.as_view({
    'delete': 'destroy'
})

request_list = view.RequestViewSet.as_view({
    'get': 'list'
})

request_create = view.RequestViewSet.as_view({
    'post': 'create'
})

request_retrieve = view.RequestViewSet.as_view({
    'get': 'retrieve'
})

request_delete = view.RequestViewSet.as_view({
    'delete': 'destroy'
})

review_list = view.ReviewViewSet.as_view({
    'get': 'list'
})

review_create = view.ReviewViewSet.as_view({
    'post': 'create'
})

review_retrieve = view.ReviewViewSet.as_view({
    'get': 'retrieve'
})

review_delete = view.ReviewViewSet.as_view({
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('user/', user_list, name='user-list'),
    path('user/<int:pk>', user_retrieve, name='user-retrieve'),
    path('user/create', user_create, name='user-create'),
    path('user/<int:pk>/delete', user_delete, name='user-delete'),

    path('service/', service_list, name='service-list'),
    path('service/<int:pk>', service_retrieve, name='service-retrieve'),
    path('service/create', service_create, name='service-create'),
    path('service/<int:pk>/delete', service_delete, name='service-delete'),

    path('request/', request_list, name='request-list'),
    path('request/<int:pk>', request_retrieve, name='request-retrieve'),
    path('request/create', request_create, name='request-create'),
    path('request/<int:pk>/delete', request_delete, name='request-delete'),

    path('review/', review_list, name='review-list'),
    path('review/<int:pk>', review_retrieve, name='review-retrieve'),
    path('review/create', review_create, name='review-create'),
    path('review/<int:pk>/delete', review_delete, name='review-delete'),
])
