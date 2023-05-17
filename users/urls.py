# from django.urls import path
# from .views import login_view, register_user
# from django.contrib.auth.views import LogoutView

# urlpatterns = [
#     path('login/', login_view, name="login"),
#     # path('register/', register_user, name="register"),
#     path('logout/', LogoutView.as_view(), name="logout")
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     # Autres URLs de l'application
#     path('users/', views.user_list, name='user_list'),
# ]



from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view' ),
    path('register/', views.register_view, name='register_view' ),
    
    path('dashboard/', views.dashboard, name='dashboad' ),
    path('edit/', views.editProfile, name='edit_profie' ),
]
