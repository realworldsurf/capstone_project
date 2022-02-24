# import views 
from. import views

from django.urls import path, include


# Create your views here.

app_name = 'post_app'

urlpatterns = [ # home page is and empty path to local host
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('messages/', views.messages, name='messages'),
    path('inbox/', views.inbox, name='inbox'),
    path('posts/<int:post_id>', views.detail, name='detail'),
    path('delete/<int:post_id>', views.delete, name='delete'),
    path('like/<int:pic_id>', views.like, name='like'),
]