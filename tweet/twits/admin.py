from django.contrib import admin
from .models import Twit, Comment
# Register your models here.
@admin.register(Twit)
class TwitAdmin(admin.ModelAdmin):
    list_display=('user', 'image', 'created_date',)
    list_filter=('user', 'created_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('twit','user', 'created_datetime',)
    list_filter=('user', 'created_datetime',)

