from django.contrib import admin

# Register your models here.

from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('prenom','nom','email','message','date_creation')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','miniature','auteur','date_creation','date_mise_a_jour')


admin.site.register(Article,ArticleAdmin)

admin.site.register(Contact, ContactAdmin)
