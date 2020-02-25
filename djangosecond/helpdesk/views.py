from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import View
from bootstrap_modal_forms.mixins import PassRequestMixin
from .forms import CreateIssueForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from dal import autocomplete
from .models import Issue, Component, Status
from django.utils.html import format_html

class Home(autocomplete.Select2QuerySetView):
    # def get_result_label(self, item):
    #     return format_html('<div style="color: red;">{}</div>', item.component)

    def get_result_value(self, result):
        return str(result.component)

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Issue.objects.none()

        qs = Component.objects.all()

        if self.q:
            qs = qs.filter(component__istartswith=self.q)

        return qs


def home(request):

    if request.method == 'POST':
        form = CreateIssueForm(request.POST)
        form.instance.reporter = request.user
        form.instance.status = Status.objects.all().filter(status='Waiting for support').first()
        if form.is_valid():
            messages.success(request, "success")
            form.save()
        return redirect('home')
    return render(request, 'helpdesk/home.html', {'form': CreateIssueForm})

def user(request, *args, **kwargs):

    if request.method == 'POST':
        messages.success(request, request.POST.get('username'))
        x = request.POST.get('username')
        return redirect(reverse('profile', kwargs={'username': x}))
    return render(request, 'helpdesk/user.html')

