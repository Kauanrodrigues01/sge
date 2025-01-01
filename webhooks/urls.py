from django.urls import path
from . import views

app_name = 'webhooks'

urlpatterns = [
    path('edit-webhook/', views.edit_webhook_config, name='edit_webhook_config'),
]
