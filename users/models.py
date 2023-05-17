# # from django.db import models
# # from django.contrib.auth.models import AbstractUser


# # # Create your models here.


# # class CustomUser(AbstractUser):
# #     user_type_data=((1,"ADMIN"), (2,"CLIENT"))
# #     user_type=models.CharField(default=1,choices=user_type_data,max_length=20)

# # class Admin(models.Model):
# #     id=models.AutoField(primary_key=True)
# #     admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
# #     created_at=models.DateTimeField(auto_now_add=True)
# #     updated_at=models.DateTimeField(auto_now_add=True)
# #     objects=models.Manager()


# # class Client(models.Model):
# #     id=models.AutoField(primary_key=True)
# #     client=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
# #     address=models.TextField()
# #     created_at=models.DateTimeField(auto_now_add=True)
# #     updated_at=models.DateTimeField(auto_now_add=True)
# #     objects=models.Manager()

# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have a username")

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username"]

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_superuser(self):
#         return self.is_admin

#     @property
#     def is_staff(self):
#         return self.is_staff

# from django.contrib.auth.models import Group

# admin_group = Group(name='Administrators')
# admin_group.save()

from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


# User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/img/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return 'Profile of %s' % self.user.username
    