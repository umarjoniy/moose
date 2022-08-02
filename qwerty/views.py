from django.shortcuts import render
from .models import *
from .forms import ContactForm
from .models import Subscribe


def index(request):
    posts = Article.objects.filter(is_published=True)[:6]
    context = {
        'page_id': 1,
        'posts': posts
    }
    return render(request, 'index.html', context)


def blog(request):
    tags = Tag.objects.all()
    posts = Article.objects.filter(is_published=True).order_by('-id')
    context = {
        'page_id': 2,
        'posts': posts,
        'tags': tags
    }
    tag = request.GET.get('tag')

    if tag:
        tag_obj = Tag.objects.get(name=tag)
        posts = Article.objects.filter(tag=tag_obj)

        context = {
            'page_id': 2,
            'posts': posts,
            'tags': tags
        }
    return render(request, 'blog.html', context)


def about(request):
    data = About.objects.get()
    ctx = {
        'data': data
    }
    return render(request, 'about.html', ctx)


def contact(request):
    # if request.method == 'POST':
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    email = request.POST.get('email')
    if email:
        Subscribe.objects.create(email=email)
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def blog_single(request, slug):
    post = Article.objects.get(slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')
        Comment.objects.create(article=post, name=name, email=email, website=website, message=message)

    comments = Comment.objects.filter(article=post)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog-single.html', context)


def index2(request):
    return render(request, 'index-2.html')
