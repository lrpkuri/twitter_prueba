""" Model for tuiti."""
from  django.contrib.auth.models import User
from django.db import models


class Tuiti(models.Model):
    """ Class of a Tuiti."""

    user = models.OneToOneField(User)
    message = models.CharField(max_length=240)
    date_tuiti = models.DateTimeField(auto_now_add=True)
    multimedia = models.ImageField(upload_to="media/tuit_pics", null=True, blank=True)
    total_likes = models.IntegerField(default=0)
    total_retuits = models.IntegerField(default=0)

    def __str__(self):
        """Return tuiti message and user."""
        return "Tuiti by {user}, {date_tuiti}".format(
            user=self.user,
            date_tuiti=self.date_tuiti,
        )
