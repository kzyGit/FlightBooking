from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, first_name, sur_name, email,
                    nationality, id_or_passport, password, middle_name=None):
        email = self.normalize_email(email)
        self.first_name = first_name
        self.middle_name = middle_name
        self.sur_name = sur_name
        self.nationality = nationality
        self.id_or_passport = id_or_passport
        self.password = password

        user = self.model(
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            sur_name=sur_name,
            nationality=nationality,
            id_or_passport=id_or_passport,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_Admin(self, first_name, middle_name, sur_name, email,
                     nationality, id_or_passport, password):
        user = self.create_user(first_name, middle_name,
                                sur_name, email, nationality, id_or_passport,
                                password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Users model """
    first_name = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length=100, null=True)
    sur_name = models.CharField(max_length=100, null=False)
    nationality = models.CharField(max_length=100, null=False)
    id_or_passport = models.IntegerField(unique=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'sur_name',
                       'nationality', 'id_or_passport', 'password']

    def __str__(self):
        """ Instance presentation """
        return "yesss"
