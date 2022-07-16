from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .form import BlogForm, CommentForm
from .models import BlogComment, BlogModel, Category, Profile


def home(request):
    # blogs= BlogModel.objects.all().order_by('-created_at')
    # blogs = BlogModel.objects.filter(category__slug=slug)
    categories = Category.objects.all()

    if request.method =='POST':
        search = request.POST.get('search')
        results = BlogModel.objects.filter(Q(title__icontains=search)|Q(sub_title__icontains=search))                           
        # results = BlogModel.objects.filter(Q(title__icontains=search)|Q(content__icontains=search))                           
        context =  { 'results': results, 'search': search,'categories': categories}
        return render(request, 'blog/index.html', context)

    #pagination
    blog_pagi= BlogModel.objects.all().order_by('-created_at')
    paginator = Paginator(blog_pagi, 10)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)


    context = {
                'blogs' : blogs,
                'categories': categories,
                }
    return render(request, 'blog/home.html',context)


def category(request, slug):
    allblogs = BlogModel.objects.filter(category__slug=slug)
    categories = Category.objects.all()
    context =  { 
                'allblogs': allblogs,
                'categories': categories,
        }
    return render (request, 'blog/category.html', context)



def register(request):
    return render(request, 'blog/register.html')

def index(request):
    blogs= BlogModel.objects.all().order_by('-created_at')
    context = {'blogs' : blogs}
    return render(request, 'blog/index.html',context)


def logout_view(request):
    logout(request)
    return redirect("login")

def login(request):
    return render(request, 'blog/login.html')




def blog_detail(request, slug):
    blog_obj = BlogModel.objects.filter(slug = slug).first()
    comments = blog_obj.blogcomment_set.all()
    total_comment = comments.count()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog_obj
            comment.author = request.user
            comment.save()
            messages.success(request,"commnet added successfully")

            context = {
                'blog_obj' : blog_obj,
                'comments': comments,
                'total_comment' : total_comment,

            }

            return render(request, 'blog/blog_detail_with_comment.html', context)

    else:
        form = CommentForm()

    context = {
        'blog_obj' : blog_obj,
        'form' : form,
        'comments': comments,
        'total_comment' : total_comment,

    }

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
    categories = Category.objects.all()
    context = {'form' : BlogForm, 'categories': categories}
    
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            sub_title = request.POST.get('sub-title')
            category_id= request.POST.get('category')
            # print("i find category ", category_id)
            user = request.user
        
            if form.is_valid():
                content = form.cleaned_data['content']

            category = Category.objects.filter(id=category_id).first()
            print("category last = ", category)
            blog_obj = BlogModel.objects.create(
                user = user, 
                title = title, 
                sub_title =sub_title,
                category=category, 
                content = content, 
                image = image
            )
            messages.success(request, "Congratulations! Post Complete.")
            print(blog_obj)
            return redirect('/add-blog/')
            
    except Exception as e :
        print(e)
    return render(request , 'blog/add_blog.html', context)

@login_required(login_url='login')
def blog_delete(request, id):
    blog_obj = get_object_or_404(BlogModel, id=id)
    if request.method == 'POST':
        blog_obj.delete()
        messages.success(request, "Post Delete Completed!")
        return redirect('see_blog')
    context ={'blog_obj': blog_obj}
    return render (request, 'blog/delete.html', context)


@login_required(login_url='login')
def blog_update(request, slug):
    categories = Category.objects.all()
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
            blog_obj.sub_title = request.POST.get('sub-title')
            blog_obj.category_id= request.POST.get('category')
            blog_obj.user = request.user  
        
            if form.is_valid():
                blog_obj.content = form.cleaned_data['content']
            blog_obj.save()
            messages.success(request, f"Blog updated successfully!")
            return redirect('/')
        context = {'blog_obj':blog_obj,'form':form, 'categories':categories }
        
    
    except Exception as e :
        print(e)
    return render(request, 'blog/update_blog.html', context)


@login_required(login_url='login')  
def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()
        if profile_obj:
           profile_obj.is_verified=True
           profile_obj.save()
            # messages.success(request, f"Your account successfully Verifyed!")
        return redirect('/login/')

    except Exception as e : 
        print(e)
    
    return redirect('/')

