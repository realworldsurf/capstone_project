from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from .models import Post, Message

from .forms import PostForm, MessageForm
# @login_required
from django.contrib.auth.decorators import login_required
from django .urls import reverse
from django.http import JsonResponse
from django.http.response import JsonResponse
# Create your views here.


#Home
def home(request):
    # all to render all the posts, "".order_by('-date_created')" descending order by newest on top
    posts = Post.objects.all().order_by('-date_created')
    #print(posts)
    context = {
        'posts':posts
    }

    return render(request, 'posts/home.html', context)

   
@login_required
def create(request):
    if request.method == 'GET': 

        form = PostForm()

        context = {
        'form': form
        }
        return render(request, 'posts/create.html', context)

    elif request.method == 'POST' and 'image' in request.FILES:
        form = PostForm(request.POST)
        image = request.FILES.get('image')
        if image:
            form.initial['image'] = image
        #['images'] implement later
        #form.initial['comment'] = request.FILES.get('comment')
        print(request.POST)
        print(request.FILES)
# redirects to the home page if there are no errorts.
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
        return redirect(reverse('post_app:home'))



def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detail.html', {'post': post})





@login_required
def messages(request):
    post_id = get_object_or_404(Post, id=post_id)
    post_id = Message.objects.filter(recipient=request.user)
    messages = {}
    for message in messages:
        if message.sender not in messages:
            messages[message.sender] = [message]
        else:
            messages[message.sender].append(message)

    return render(request, 'inbox/inbox.html', {'post_id': post_id})




@login_required
def inbox(request):
    if request.method == 'GET': 
        post_id = request.GET.get('post_id')
        print('pos_id', post_id)
        #print(request.POST.get.post_id)
        form = MessageForm()
             
        context = {
            'form': form,
            'post_id': post_id,
        }
        return render(request, 'inbox/inbox.html', context)

    elif request.method == 'POST':
        post_id = request.POST.get('post_id')
        form = MessageForm(request.POST)
        print('---------------------')
        #['images'] implement later
        #form.initial['comment'] = request.FILES.get('comment')
        print(request.POST)
        #print(request.FILES)
        print(post_id)
# redirects to the home page if there are no errorts.
        if form.is_valid():
            #sender, receiver, post id
            #new_message = form.save(commit=False)
            new_message = form.save(commit=False)
            new_message = form.save()
            #new_message.user = request.user
            #new_message.save()
        return redirect(reverse('post_app:inbox'), {'post_id':post_id})



def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect(reverse('post_app:home'))



    
@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id) 
    if request.user not in post.likes.all(): 
        post.likes.add(request.user)
    else: 
        post.likes.remove(request.user)
    return redirect(reverse(request, 'job_app:home'))

