from django import forms

from .models import Post, Message

from django.forms import widgets

class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post 
        fields = [
            'image',
            'job_title',
            'job_summary',
            'job_description',
            'skills',
            'location',
            'hours', 
            'remote_type',
            'job_categories',
   
         ]
# widgets are not working at this time 3/3/2022
"""
widgets = {
    'comment': forms.Textarea(attrs={'class':'form-control', 'style': 'resize=none; white-space: pre-wrap;'}),
}
"""

#import into view

class MessageForm(forms.ModelForm): 
    class Meta: 
        model = Message 
        fields = [
            #'image',
            #'post_id',
            'message_text',  
   
         ]

