from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Article
from .models import Contact
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import *
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

def accueil(request):
    # Récupérer les 4 derniers articles du blog
    latest_articles = Article.objects.order_by('date_creation')[:4]
    context = {
        'articles': latest_articles,
    }
    
    return render(request, 'accueil.html', context)



def blog(request):
    articles_list = Article.objects.all().order_by('date_creation')
    paginator = Paginator(articles_list, 5) # 5 articles par page
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'blog.html', {'articles': articles})



def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    context = {'article': article}
    return render(request, 'detail.html', context)





@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect(reverse('blog'))
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

@login_required
def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'edit_article.html', {'form': form})


def about(request):
    return render(request, "about.html")


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            return redirect(reverse('blog'))
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
