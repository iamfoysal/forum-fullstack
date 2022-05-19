from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .form import *
from django.contrib.auth import logout
from django.contrib import messages



def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, 'blog/home.html',context)


def register(request):
    return render(request, 'blog/register.html')


def logout_view(request):
    logout(request)
    messages.success(request, "logout successfully Complete.")
    return redirect("login")

def login(request):
    return render(request, 'blog/login.html')





def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request , 'blog/blog_detail.html' , context)



@login_required(login_url='login')
def see_blog(request):
    context = {}
    
    try:
        blog_object = BlogModel.objects.filter(user = request.user)
        context['blog_object'] =  blog_object
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'blog/see_blog.html' ,context)


@login_required(login_url='login')
def add_blog(request):
    
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )
            print(blog_obj)
            return redirect('/add-blog/')
            
    except Exception as e :
        print(e)
    return render(request , 'blog/add_blog.html', context)

def blog_delete(request, id):
    blog_obj = get_object_or_404(BlogModel, id=id)
    if request.method == 'POST':
        blog_obj.delete()
        return redirect('see_blog')
    context ={'blog_obj': blog_obj}
    return render (request, 'blog/delete.html', context)



def blog_update(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(slug = slug)

        if blog_obj.user != request.user:
            return redirect('/') 
    
        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial = initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            blog_obj.image = request.FILES['image']
            blog_obj.title = request.POST.get('title')
            blog_obj.user = request.user  
        
            if form.is_valid():
                blog_obj.content = form.cleaned_data['content']
            blog_obj.save()
            messages.success(request, f"Blog updated successfully!")
            return redirect('/')
        
        context['blog_obj'] = blog_obj
        context['form'] = form
    
    except Exception as e :
        print(e)
    return render(request, 'blog/update_blog.html', context)
   
def verify(request,token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()
        
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e : 
        print(e)
    
    return redirect('/')