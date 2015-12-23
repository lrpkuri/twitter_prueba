"""Models for useraccounts."""
from  django.contrib.auth.models import User
from django.db import models
from tuiti.models import Tuiti


class UserSettings(models.Model):
    """Settings of users."""

    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to="media/profile_pictures")
    cover_picture = models.ImageField(upload_to="media/cover_pictures")
    is_private = models.BooleanField(default=False)

    def __str__(self):
        """Return tuiti message and user."""
        return "Settings of user."


class UserFollowsUser(models.Model):
    """Class to identify a user."""

    followed = models.OneToOneField(User, related_name='followed')
    follower = models.OneToOneField(User, related_name='follower')
    date_follow = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return follower and followed."""
        return "{follower} is following {followed}".format(
            follower=self.follower,
            followed=self.followed,
        )


class UserLikesTuiti(models.Model):
    """User likes tuit."""

    user = models.OneToOneField(User)
    tuiti = models.OneToOneField(Tuiti)
    date_like = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return name of user that liked tuit."""
        return "{user} liked {tuiti_user} tuiti".format(
            user=self.user,
            tuiti_user=self.tuiti.user,
        )
