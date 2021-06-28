from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):

    def create_user(self, email, fullName, password, universty, department, account_type):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            fullName=fullName,
            universty=universty,
            department=department,
            account_type=account_type,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, fullName, universty, department, account_type):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            fullName=fullName,
            universty=universty,
            department=department,
            account_type=account_type

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    accType = (

        ('accType1', 'Öğrenci'),
        ('accType2', 'Akademisyen')
    )

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    universty = models.CharField(max_length=250)
    fullName = models.CharField(max_length=30)
    department = models.CharField(max_length=250)
    account_type = models.CharField(
        max_length=10, choices=accType, default='accType1')
    account_avatar = models.FileField(
        blank=True, null=True, verbose_name='Fotoğraf ekle')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName', 'universty', 'department', 'account_type']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
