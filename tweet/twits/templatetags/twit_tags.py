from atexit import register
from django import template
from actions.models import Action
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404


register=template.Library()

@register.simple_tag
def comments(twit):
    comments=twit.twit_comments.all()
    return comments

@register.simple_tag
def twit_add(target):
    target_ct=ContentType.objects.get_for_model(target)
    action=get_object_or_404(Action, target_ct=target_ct, target_id=target.id)
    return action