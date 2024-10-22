from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):
    # Fields below will be asked when user is created
    def create_user(self, first_name, last_name, username, email, password):
        if not email:
            raise ValueError('email field was not provided!')
        
        
        if not username:
            raise ValueError('username field was not provided!')

        # self.model refers to User in this case
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, first_name, last_name, username, email, password):
        # in order to create superuser we need to actually create it and then make it superuser
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        
        user.save(using=self._db)
        return user
             


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)

    # Required Fields (because we override AbstractBaseUser)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    
    
    
    USERNAME_FIELD = 'email' # instead of username email will be asked
    # WE DON'T NEED EMAIL HERE BECAUSE email IS ALREADY REQUIRED FIELD!
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = UserManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        # Returns True if the user has any permissions in the given package 
        # (the Django app label). If the user is inactive, this method will 
        # always return False. For an active superuser, this method will always return True.

        return True
