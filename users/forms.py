# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# # class LoginForm(forms.Form):
# #     username = forms.CharField(label="Nom d'utilisateur", 
# #                                widget=forms.TextInput(
# #                                     attrs={
# #                                         "class": "form-control"
# #                                 }))
# #     password = forms.CharField(label="Mot de passe", 
# #                                widget=forms.PasswordInput(
# #                                     attrs={
# #                                         "class": "form-control"
# #                                 }))

# # class SignUpForm(UserCreationForm):
# #     username = forms.CharField(label="Nom d'utilisateur", 
# #                                widget=forms.TextInput(
# #                                     attrs={
# #                                         "class": "form-control"
# #                                 }))
# #     email = forms.EmailField(label="email", 
# #                                widget=forms.EmailInput(
# #                                     attrs={
# #                                         "class": "form-control"
# #                                 }))
# #     password1 = forms.CharField(label="Mot de passe", 
# #                                widget=forms.PasswordInput(
# #                                     attrs={
# #                                         "class": "form-control"
# #                                 }))
# #     password2 = forms.CharField(label="Confirmation de mot de passe", 
# #                                widget=forms.PasswordInput(
# #                                     attrs={
# #                                         "class": "form-control"
# #                                 }))
# #     class Meta:
# #         model = User
# #         fields =('username', 'email', 'password1', 'password2') 
        
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import User

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'email']

# from django import forms
# from django.contrib.auth.forms import AuthenticationForm

# class CustomAuthenticationForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']


from django import forms 
from django.contrib.auth.models import User

from users.models import Profile


class RegistrationForm(forms.ModelForm):
	username = forms.CharField(label="Username", max_length=250, help_text='', required=True, 
							   widget=forms.TextInput(attrs={"class":"form-control", "id":"username",  "type":"text",  "placeholder":"Username", "data-sb-validations":"required"}) )
	
	first_name = forms.CharField(label="first_name", max_length=250, help_text='', required=True, 
							   widget=forms.TextInput(attrs={"class":"form-control", "id":"first_name",  "type":"text",  "placeholder":"First Name", "data-sb-validations":"required"}) )
	
	last_name = forms.CharField( label='last_name', 
							   max_length=250, min_length=3, 
							   help_text='',
							   required=True, 
							   widget=forms.TextInput(attrs={"class":"form-control", "id":"last_name", "type":"text", "placeholder":"Last Name", "data-sb-validations":"required"})
							   )
	email = forms.EmailField( label='email', 
							   max_length=250, min_length=5, 
							   help_text='',
							   required=True, 
							   widget=forms.TextInput(attrs={"class":"form-control", "id":"email", "type":"email", "placeholder":"Email Address", "data-sb-validations":"required"})
							   )
	password = forms.CharField( label='password', 
							   max_length=250, min_length=8, 
							   help_text='',
							   required=True, 
							   widget=forms.TextInput(attrs={"class":"form-control", "id":"password", "type":"password", "placeholder":"Password", "data-sb-validations":"required"})
							   )
	confirm_password = forms.CharField( label='confirm_password', 
							max_length=250, min_length=8,
							help_text='',
							required=True, 
							widget=forms.TextInput(attrs={"class":"form-control", "id":"confirm_password", "type":"password", "placeholder":"Confirm Password", "data-sb-validations":"required"})
							)
 
	
	class  Meta:
		model = User
		fields = ('username', "first_name", 'last_name', 'email')
  
  
	def clean_confirm_password(self):
		cd = self.cleaned_data
		if cd['password'] != cd['confirm_password']:
			raise forms.ValidationError('les deux mots de passe ne sont pas identique')
		return cd['confirm_password']
	 
  
class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']
		
  
class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ('user',)
