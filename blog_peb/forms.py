from django import forms
from .models import Article
from .models import Contact

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('titre', 'resume', 'miniature', 'contenu', 'auteur')
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'resume': forms.Textarea(attrs={'class': 'form-control'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control'}),
            'auteur': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
        
        
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('prenom', 'nom', 'email', 'message')
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
