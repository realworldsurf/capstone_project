from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


hours_choices = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Contract', 'Contract'),
    ('Seasonal', 'Seasonal'),
    
)

remote_choices = (
    ('"Yes"', 'Remote "Yes"'),
    (' "No"', 'Remote "No"'), 
    ('Partial ', 'Partial '),
    ('No Preference', 'No Preference'),
)

shift_choices = (
    ('Day', 'Day'),
    ('Evening', 'Evening'), 
    ('Night', 'Night'),

)

availability_choices = (
    ('ASAP', 'ASAP'),
    ('1-2 months', '1-2 months'),
    ('3-4 months', '3-4 months'),
    ('5-6 months', '5-6 months'),
)


job_categories = (
    ('N/A', 'N/A'),
    ('Other', 'Other'),
    ('Accounting ', 'Accounting'),
    ('Aviation / Aerospace', 'Aviation / Aerospace'),
    ('Engineering', 'Engineering'),
    ('Child Care', 'Child Care'),
    ('Clerical / Office', 'Clerical / Office'),
    ('Communications', 'Communications'),
    ('Construction', 'Construction'),
    ('Computer / Software Enginner', 'Computer / Software Engineer'),
    ('Customer Service', 'Customer Service'),
    ('Education / Teaching', 'Education /Education'),
    ('Federal / State / Civil Government', 'Federal / State / Civil Government'),
    ('Helthcare / Medical', 'Healthcare / Medical'),
    ('Human Resources', 'Human Resources'),
    ('Legal', 'Legal'),
    ('Management', 'Management'),
    ('Mechanic', 'Mechanic'),
    ('Marketing', 'Marketing'),
    ('Sales', 'Sales'),
    ('Social Work', 'Social Work'),
    ('Real Estate', 'Real estate'),
    ('Transportation', 'Transportation'),
    ('Work From Home', 'Work From Home'),
    ('Other', 'Other'),
    ('N/A', 'N/A'),
    
)
'''
# SALARY RANGE
salary_range = (
    (),
)
'''
def get_upload_path(instance, filename):
        return f'images/user_images/{filename}'




class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    job_summary = models.CharField(max_length=150, null=True, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    job_title = models.CharField(max_length=150)
    job_description = models.CharField(max_length=1000)
    skills = models.CharField(max_length=1000)
    #skills = models.ManyToManyField()
    #resume = models.FileField(upload_to='resumes', null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    hours = models.CharField(
        max_length=30, choices=hours_choices, default='Full Time', null=True)
    remote_type = models.CharField(
        max_length=30, choices=remote_choices, default='No Preference', null=True)
    job_categories = models.CharField(
        max_length=50, choices=job_categories, default='N/A', null=True)
    likes = models.ManyToManyField(get_user_model(), related_name='users', blank=True)


    def __str__(self):
        return self.user.username 



class Message(models.Model):
    # Foreign Key to the 'Post'
    post_id = models.ForeignKey(Post, null=True, blank=True,  on_delete=models.CASCADE, related_name='messages', default='')
    sender = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE, related_name='messages_sent')
    receiver = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE, related_name='messages_received')
    message_text = models.CharField(max_length=1500)
    #created_on = models.DateTimeField(auto_now_add=True)
    
 
    def __str__(self):
        return self.message_text

class Inbox(models.Model):
    # Foreign key to the 'Message'
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='inbox')
    messages = models.ForeignKey(Message, null=True, on_delete=models.CASCADE, related_name='inbox')
    


    def __str__(self):
        return self.user.username 



        # set 3 values to save the form from admin change message