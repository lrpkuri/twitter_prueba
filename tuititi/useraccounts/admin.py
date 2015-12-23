"""User settings admin."""

from django.contrib import admin

from useraccounts.models import UserSettings, UserFollowsUser


@admin.register(UserSettings)
class SettingsAdmin(admin.ModelAdmin):
    """Settings Admin."""

    list_display = ('user', 'profile_picture', 'cover_picture', 'is_private')


@admin.register(UserFollowsUser)
class FollowerAdmin(admin.ModelAdmin):
    """Follows."""

    list_display = ('followed', 'follower', 'date_follow')