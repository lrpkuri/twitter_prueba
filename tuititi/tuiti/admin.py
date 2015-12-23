from django.contrib import admin

from tuiti.models import Tuiti


@admin.register(Tuiti)
class TuitiAdmin(admin.ModelAdmin):
    """Tuitis Admin."""

    list_display = ('user', 'message', 'total_likes', 'total_retuits', 'date_tuiti')