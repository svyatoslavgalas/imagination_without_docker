from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .forms import ImageForm


@login_required
def upload_image(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        data = {'result': False}
        if form.is_valid():
            img = form.save(commit=False)
            img.user = request.user
            img.save()
            user_email = img.user.email
            msg = '{};{};{};'.format(user_email, img.date_time, img.image)
            send_mail(
                'Подтверждение об сохранении изображения',
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


