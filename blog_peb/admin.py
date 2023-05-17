from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import *
# from users.models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('prenom','nom','email','message','date_creation')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','miniature','auteur','date_creation','date_mise_a_jour')


admin.site.register(Article,ArticleAdmin)

admin.site.register(Contact, ContactAdmin)

# admin.site.register(Profile,UserAdmin)


