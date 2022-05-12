from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from core.models import User, Review, Service
from django.shortcuts import render, reverse


class UserListView(ListView):
    model = User
    template_name = 'api/list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'api/detail.html'
    context_object_name = 'user'


class UserCreateView(CreateView):
    model = User
    template_name = 'api/create.html'
    fields = ('fullname', 'phone', 'email', 'role')
    success_url = reverse_lazy('user-list')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'api/update.html'
    context_object_name = 'user'
    fields = ('fullname', 'phone', 'email', 'role')

    def get_success_url(self):
        return reverse('user-detail', kwargs={'pk': self.object.id})


class UserDeleteView(DeleteView):
    model = User
    template_name = 'api/delete.html'
    success_url = reverse_lazy('user-list')
