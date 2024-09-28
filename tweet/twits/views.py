from hashlib import new
from django.shortcuts import render, get_object_or_404
from .models import Twit, Comment
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import TwitForm, CommentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from actions.utils import create_action
from actions.models import Action

# Create your views here.
@login_required
def list_twits(request, user_id=None):
    if user_id:
        user=get_object_or_404(User, id=user_id)
        twits=user.twits.all()
        return render(request, 'twits/user_twits.html',{'twits':twits, 'user':user})
    else:
        twits=Twit.objects.all()
    #dd(actions)
    return render(request, 'twits/list_twits.html',{'twits':twits,})

def add_twit(request):
    if request.method=='POST':
        twit_form=TwitForm(data=request.POST, files=request.FILES)
        if twit_form.is_valid():
            new_twit=twit_form.save(commit=False)
            user=request.user
            new_twit.user=user
            new_twit.save()
            create_action(request.user, 'twited', new_twit)
            messages.success(request, 'Created successfully!')
        else:
            messages.error(request, 'Error creating twit.')
    else:
        twit_form=TwitForm()
    return render(request,'twits/add_twit.html', {'twit_form':twit_form})

def add_comment(request, twit_id):
    twit=get_object_or_404(Twit, id=twit_id)
    if request.method=='POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            user=request.user
            new_comment.user=user
            new_comment.twit=twit
            new_comment.save()
            messages.success(request, 'Created successfully!')
        else:
            messages.error(request, 'Error creating comment.')
    else:
        comment_form=CommentForm()
    return render(request, 'twits/add_comment.html', {'comment_form': comment_form})

def list_users(request):
    users=User.objects.all()
    return render(request, 'twits/list_users.html', {'users':users})

@ajax_required
@login_required
@require_POST
def twit_like(request):
    twit_id = request.POST.get('id')
    action = request.POST.get('action')
    if twit_id and action:
        try:
            twit = Twit.objects.get(id=twit_id)
            if action == 'like':
                twit.users_like.add(request.user)
            else:
                twit.users_like.remove(request.user)
            return JsonResponse({'status':'ok', 'user':request.user.username})
        except:
            pass
    return JsonResponse({'status':'error'})