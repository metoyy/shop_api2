from django.core.mail import send_mail

def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здраствуйте, активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке:'
        f'\n{full_link}'
        f'\nНе передаватйте этот код никому!',
        'bekurudinov@gmail.com',
        [user],
        fail_silently=False,

    )


