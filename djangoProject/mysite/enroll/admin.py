from django.contrib import admin

# Register your models here.

from .models import Participant, LoginToken

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'email',
        'others_can_see_me',
        'participating'
    )
    search_fields = ['last_name', 'first_name', 'email']

@admin.register(LoginToken)
class Tokenadmin(admin.ModelAdmin):
    list_display = (
        'token',
        'name',
        'email',
        'created'
    )

    def name(self, instance):
        return instance.participant.name()

    def email(self, instance):
        return instance.participant.email
