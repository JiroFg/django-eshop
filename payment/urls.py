from django.urls import path
from .views import payment_process, payment_completed, payment_canceled
from django.utils.translation import gettext_lazy as _

app_name = 'payment'

urlpatterns = [
    path(_('process/'), payment_process, name='process'),
    path(_('completed/'), payment_completed, name='completed'),
    path(_('canceled/'), payment_canceled, name='canceled'),
]
