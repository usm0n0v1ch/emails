from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            full_message = f"Имя: {name}\nEmail: {email}\nСообщение: {message}"

            try:
                send_mail(
                    'Контактная форма',
                    full_message,
                    settings.EMAIL_HOST_USER,
                    ['dilmurodtagandurdiyev@gmail.com'],
                    fail_silently=False
                )
                messages.success(request, 'Письмо отправлено успешно!')
            except Exception as e:
                messages.error(request, f'Ошибка при отправке письма: {e}')
        else:
            messages.error(request, 'Все поля должны быть заполнены!')

    return render(request, 'app/index.html')
