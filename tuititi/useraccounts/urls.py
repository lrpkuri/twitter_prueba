"""User Accounts URLs."""

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(
        r'^$',
        TemplateView.as_view(
            template_name='useraccounts/login.html'
        ),
        name='login'
    ),
    url(
        r'^user_(?P<user>\d+)/$',
        TemplateView.as_view(
            template_name='useraccounts/profile.html'
        ),
        name='profile'
    ),
    url(
        r'^settings/$',
        TemplateView.as_view(
            template_name='useraccounts/settings.html'
        ),
        name='settings'
    ),
]
 