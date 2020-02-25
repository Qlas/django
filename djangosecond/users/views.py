from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django import http
from .token_generator import account_activation_token
from django.contrib.auth import login, authenticate
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

def register(requet):
    if requet.user.is_authenticated:
        messages.info(requet, f'You are logged in!')
        return redirect('home')

    if requet.method == 'POST':
        form = UserRegisterForm(requet.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            token = account_activation_token.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.id))

            username = form.cleaned_data.get('username')
            current_site = get_current_site(requet)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()

            messages.success(requet,f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(requet, 'users/register.html', {'form': form})

@login_required
def account(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form' : u_form,
        'p_form': p_form
    }
    return render(request, 'users/account.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, f'Your account has confirm, log in!')
        return redirect('login')
    else:
        messages.warning(request, f'Activation link is invalid!')
        return redirect('home')


