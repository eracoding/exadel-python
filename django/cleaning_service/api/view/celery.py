from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from api.forms import GenerateRandomUserForm
from api.tasks import create_users


class GenerateRandomUserView(FormView):
    form_class = GenerateRandomUserForm
    template_name = 'api/userUpdate.html'

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_users.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('userCrud-list')
