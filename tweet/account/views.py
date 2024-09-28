from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile, Contact
from django.contrib import messages
from PIL import Image
from common.decorators import ajax_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse


# Create your views here.
@login_required
def dashboard(request):
    return render(
        request,
        'account/dashboard.html',
        {'section':'dashboard'}
    )

def register(request):
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            cd=user_form.cleaned_data
            new_user=user_form.save(commit=False)
            new_user.set_password(cd['password2'])
            new_user.save()
            Profile.objects.create(user=new_user)
            messages.success(request, 'Account created successfully!')
            return render(request,
                        'account/register_done.html',
                        {'new_user':new_user})
        else:
            messages.error(request, 'Error creating an account.')
    else:
        user_form=UserRegistrationForm()
    return render(request,
                    'account/register.html',
                    {'user_form':user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        #dd(profile_form)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})

@ajax_required
@login_required
@require_POST
def user_follow(request):
    user_id=request.POST.get('id')
    action=request.POST.get('action')
    
    if user_id and action:
        try:
            user=User.objects.get(id=user_id)
            if action=='follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'error'})
    return JsonResponse({'status':'error'})
