from django.forms import ModelForm
from enroll.models import Participant

class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'others_can_see_me']