from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from users.forms import ProfileEditForm, RegistrationForm, UserEditForm
from users.models import Profile
# Create your views here.


def login_view(request):
    if not  request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accueil')
            else: 
                return render(request, 'login.html', {})
        else:
            return render(request, 'login.html', {})
    else:
        return redirect('accueil')
           
        

def logout_view(request):
    logout(request)
    return redirect('accueil')
        


def register_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login_view')
        else:
            return render(request, 'register.html', {'user_form': user_form})
    else:
        user_form = RegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})



@login_required
def dashboard(request):
    user = Profile.objects.filter(user=request.user).first()
    return render(request, 'dashboard.html', {'user': user})


@login_required
def editProfile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, 
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                      data=request.POST,
                                      files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboad')
    else:
        user_form = UserEditForm(instance=request.user, 
                                 )
        profile_form = ProfileEditForm(instance=request.user.profile,
                                      )
    return render(request, 'edit.html', {'user_form': user_form,
                                        'profile_form': profile_form})