from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post
def index(request):
    all_post = Post.objects.all()
    return render(request,'index.html',{'all_post':all_post})


def create(request):
    if request.method == "POST":
        create_form = PostForm(request.POST,request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('index')
    else:
        create_form = PostForm()
    return render(request,'create.html',{'create_form':create_form})

def detail(request,post_id):
    my_post = Post.objects.get(id=post_id)
    return render(request,'detail.html',{'my_post':my_post})

def update(request,post_id):
    context = dict()
    my_post = Post.objects.get(id=post_id)
    context['my_post'] = my_post
    if request.method == "POST":
        update_form = PostForm(request.POST,request.FILES,instance=my_post)
        if update_form.is_valid():
            update_form.save()
            return redirect('detail',post_id)
    else:
        update_form = PostForm(instance=my_post)
        context['update_form'] = update_form

    return render(request,'update.html',context)

def delete(request,post_id):
    my_post = Post.objects.get(id=post_id)
    my_post.delete()
    return redirect('index')