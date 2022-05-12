from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from core.models import User, Review, Service, Request
from django.shortcuts import render, reverse


class UserListView(ListView):
    model = User
    template_name = 'api/userList.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'api/userDetail.html'
    context_object_name = 'user'


class UserCreateView(CreateView):
    model = User
    template_name = 'api/userCreate.html'
    fields = ('fullname', 'phone', 'email', 'role')
    success_url = reverse_lazy('user-list')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'api/userUpdate.html'
    context_object_name = 'user'
    fields = ('fullname', 'phone', 'email', 'role')

    def get_success_url(self):
        return reverse('user-detail', kwargs={'pk': self.object.id})


class UserDeleteView(DeleteView):
    model = User
    template_name = 'api/userDelete.html'
    success_url = reverse_lazy('user-list')


class ReviewListView(ListView):
    model = Review
    queryset = Review.objects.filter(rating='5').all()
    template_name = 'api/reviewList.html'
    context_object_name = 'reviews'


class ServiceListView(ListView):
    model = Service
    template_name = 'api/serviceList.html'
    context_object_name = 'services'


class RequestListView(ListView):
    model = Request
    template_name = 'api/requestList.html'
    context_object_name = 'requests'
