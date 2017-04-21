import hashlib

from django.contrib import messages
from django.core import mail
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Participant, LoginToken
from .controllers.login_controller import *

def index(request):
    return render(request, 'index.html')


def user_list(request):
    participants = Participant.objects.filter(others_can_see_me=True, dropout_date=None)

    invisible = (True if not participants and Participant.objects.count() > 0 else False)

    context = dict(
        participants=participants,
        invisible=invisible,
    )
    return redirect(to='enroll:index')


def enroll(request):
    return render(request, 'enroll_form.html')


def new_participant(request):
    if request.method != 'POST':
        return enroll(request)

    email_address = request.POST['email']

    if Participant.objects.filter(email=email_address).exists():
        participant = Participant.objects.get(email=email_address)
        LoginToken.objects.filter(participant=participant).delete()
        token = LoginToken(participant=participant)
        token.save()
        send_token(request, participant.email, token)
        messages.success(request, "An account with this email exists! We sent you a login token!")
        return render(request, 'enroll_form.html')

    participant = Participant(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=email_address,
        others_can_see_me=(True if 'on' in request.POST.get('others_can_see_me', '') else False)
    )
    participant.save()

    token = LoginToken(participant=participant)
    send_token(request, participant.email, token)
    messages.success(request, "You have signed up successfully! We'll send you a login token, soon!")

    return render(request, 'enroll_form.html')


def save(request):
    if request.method != 'POST':
        return redirect(to='enroll:index')

    id_ = request.POST['id']
    participant = Participant.objects.get(id=id_)

    if not participant:
        return redirect(to='enroll:index')

    participant.first_name = request.POST['first_name']
    participant.last_name = request.POST['last_name']
    participant.others_can_see_me=(True if 'on' in request.POST.get('others_can_see_me', '') else False)

    participant.save()

    # Destroy Token?
    return redirect(to='enroll:index')


def _scramble_address(address):
    return hashlib.sha256(address.encode()).hexdigest()


def delete(request, participant_id):

    participant = Participant.objects.get(id=participant_id)

    if not participant:
        return redirect(to='enroll:index')

    participant.email = _scramble_address(participant.email)
    participant.others_can_see_me = False
    participant.dropout_date = timezone.now()
    participant.save()

    return redirect(to='enroll:index')

