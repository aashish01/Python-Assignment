from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
import uuid
from django.db.models.signals import pre_save
from Appointment.utils import unique_email_slug_Generator


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(
                email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=50,unique=True)
    name = models.CharField(max_length=155)
    address = models.CharField(max_length=155)
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "tbl_user"
        verbose_name = 'User'
        verbose_name_plural ='Users'


def hash_password(sender, instance, *args, **kwargs):

    if 'pbkdf2_sha256' in instance.password:
        pass
    else:
        instance.set_password(instance.password)
        instance.save()


pre_save.connect(hash_password, sender=User)



class DoctorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=155, null=True,blank=True, help_text="This will auto generate its value")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.email)
    
    class Meta:
        db_table = "tbl_doctor_profile"
        verbose_name = 'Doctor Profile'
        verbose_name_plural ="Doctor's Profile"


class ReceptionistProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=155, null=True,
                            blank=True, help_text="This will auto generate its value")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.email)
    
    class Meta:
        db_table = "tbl_receptionist_profile"
        verbose_name = 'Receptionist Profile'
        verbose_name_plural ="Receptionist's Profile"










# SLUG GENERATOR
def email_slug_Generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_email_slug_Generator(instance)
pre_save.connect(email_slug_Generator, sender=ReceptionistProfile)
pre_save.connect(email_slug_Generator,sender=DoctorProfile)


