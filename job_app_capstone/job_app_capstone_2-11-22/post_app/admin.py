from django.contrib import admin

# Register your models here.
from .models import Post, Inbox, Message

admin.site.register([Post, Inbox, Message])



