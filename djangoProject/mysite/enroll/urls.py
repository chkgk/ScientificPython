from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'enroll'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^enroll/', views.enroll, name='enroll'),
    url(r'^new_participant/$', views.new_participant, name='new_participant'),

    url(r'^admin/', admin.site.urls),
    url(r'^login/?$', views.login_form, name='login_form'),
    url(r'^login/(?P<token>[a-zA-Z0-9]{32})?$', views.login, name='login'),
    url(r'^request_login_token/', views.request_login_token, name='request_login_token'),

    url(r'^save/$', views.save, name='save'),
    url(r'^delete/(?P<participant_id>[0-9]+)$', views.delete, name='delete'),
]