import string
import random

from django.db import models
from django.utils import timezone


class Participant(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=400, unique=True)
    first_showup = models.DateTimeField('First Showup', default=timezone.now)
    others_can_see_me = models.BooleanField(default=False)
    dropout_date = models.DateTimeField('Dropout Date', blank=True, null=True, default=None)

    def __str__(self):
        return self.name()

    def name(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def participating(self):
        return (self.dropout_date is None)
    # http://stackoverflow.com/questions/8227023/list-display-boolean-icons-for-methods
    participating.boolean = True

    class Meta:
        ordering = ('last_name', 'first_name')


TOKEN_LENGTH = 32
def _new_token():
        alphabet = string.ascii_letters + string.digits
        return ''.join((random.choice(alphabet) for _ in range(TOKEN_LENGTH)))

class LoginToken(models.Model):
    token = models.CharField(max_length=32, unique=True, default=_new_token)
    created = models.DateTimeField(default=timezone.now)
    participant = models.OneToOneField('Participant', null=False, unique=True)

    def __str__(self):
        return self.token