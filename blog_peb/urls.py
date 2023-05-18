from django.urls import path
from .views import accueil, blog, article_detail, create_article, edit_article, about, contact


urlpatterns = [
    path('', accueil, name='accueil'),
    path('articles/', blog, name='blog'),
    path('articles/creer/', create_article, name='create_article'),
    path('articles/<int:id>/', article_detail, name='detail_article'),
    path('articles/modifier/<int:id>/', edit_article, name='modifier_article'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]



