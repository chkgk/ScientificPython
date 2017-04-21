from django.contrib import messages
from django.core import mail
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from ..models import Participant, LoginToken

TOKEN_REQUESTED = 'token_requested'

def login_form(request):
    # request.session.get(TOKEN_REQUESTED)
    # messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'login_form.html')


def login(request, token):
    # Bad Token
    if not LoginToken.objects.filter(token=token).exists():
        return redirect(to='enroll:index')

    #request.session.get(TOKEN_REQUESTED)
    # Set Login Token to Cookie

    participant = LoginToken.objects.get(token=token).participant

    if not participant.dropout_date is None:
        return redirect(to='enroll:index')

    context = dict(participant=participant)
    return render(request, 'edit_form.html', context)


def send_token(request, recipient, token):
    # Send dis shit
    BASE_URL = 'http://localhost:8000/login/'
    sender = 'johannes.hofmeister@awi.uni-heidelberg.de'
    #sender = 'jones@cessor.de'
    url = BASE_URL + token.token
    message = '''Use this key to login:\n %s'''
    message = message % url

    try:
        with mail.get_connection() as connection:
            send_mail(
                'Your Login Token',
                message,
                sender,
                [recipient],
                fail_silently=False,
                connection=connection
            )
        request.session[TOKEN_REQUESTED] = timezone.now().isoformat()
        print('Mail sent to: %s' % recipient)

    except Exception as e:
        print('An error occured while sending mail to %s\n%s' % (recipient, str(e)))
        messages.error(request, 'An error occurred!')


def request_login_token(request):
    if request.method != 'POST':
        return redirect(to='enroll:login')

    recipient = request.POST.get("email", "")
    if not recipient:
        return redirect(to='enroll:login')

    if not Participant.objects.filter(email=recipient).exists():
        messages.error(request, "I don't believe we've met...")
        return redirect(to='enroll:login')

    participant = Participant.objects.get(email=recipient)

    # Invalidate all existing tokens
    LoginToken.objects.filter(participant=participant).delete()
    token = LoginToken(participant=participant)
    token.save()

    send_token(request, recipient, token)

    messages.success(request, 'A login token has been sent to your address!')
    return redirect(to='enroll:login')