"""User Accounts URLs."""

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(
        r'^new/$',
        TemplateView.as_view(
            template_name='tuits/new_tuit.html'
        ),
        name='new_tuit'
    ),
    url(
        r'^tuit_(?P<id>\d+)/$',
        TemplateView.as_view(
            template_name='tuits/tuit_id.html'
        ),
        name='tuit_id'
    ),
]
