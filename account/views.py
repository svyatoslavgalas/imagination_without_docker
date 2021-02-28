from django.conf import settings
from django.shortcuts import render, redirect, Http404
from django.contrib import auth, messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from gallery.forms import ImageForm
from gallery.models import Image, History
from .forms import (LoginForm, SignupForm)


def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = auth.authenticate(request, email=email, password=password)
        if user:
            auth.login(request, user)
        return redirect(settings.LOGIN_REDIRECT_URL)
    ctx = {
        'form': form,
    }
    return render(request, 'account/login.html', ctx)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Вы успешно покинули сайт.')
    return redirect(settings.LOGIN_REDIRECT_URL)


def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = auth.authenticate(request, email=email, password=password)
        if user:
            auth.login(request, user)
        messages.success(request, 'Пользователь успешно зарегистрировался')
        return redirect(settings.LOGIN_REDIRECT_URL)
    ctx = {'form': form}
    return render(request, 'account/signup.html', ctx)


@login_required
def profile(request):
    ctx = {

    }
    return render(request, 'account/profile.html', ctx)


@login_required
def image_edit(request, image_id):
    image = Image.objects.get(pk=image_id)
    old_path = image.image
    if image.user.id == request.user.id:
        form = ImageForm(request.POST or None, request.FILES or None, instance=image)
        if request.method == 'POST':
            data = {'result': False}
            if form.is_valid():
                img = form.save()
                History.objects.create(
                    image=img,
                    old_path=old_path,
                )
                user_email = request.user.email
                msg = '{};{};{};'.format(user_email, img.date_time, img.image)
                send_mail(
                    'Изображение было изменено',
                    msg,
                    'info@our-site.com',
                    [user_email],
                    fail_silently=False,
                )
                data['result'] = True
            else:
                data['errors'] = form.errors
            return JsonResponse(data)
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'gallery/form.html', ctx)
    else:
        raise Http404


def image_info(request, image_id):
    image = Image.objects.get(pk=image_id)
    ctx = {
        'image': image,
    }
    return render(request, 'account/detail.html', ctx)
