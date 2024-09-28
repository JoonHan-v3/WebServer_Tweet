from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='twits'
urlpatterns=[
    path('', views.list_twits, name='list_twits'),
    path('add_twit/', views.add_twit, name='add_twit'),
    path('add_comment/<twit_id>', views.add_comment, name='add_comment'),
    path('list_users/', views.list_users, name='list_users'),
    path('user_twits/<user_id>', views.list_twits, name='user_twits'),
    path('like/', views.twit_like, name='like'),
]
