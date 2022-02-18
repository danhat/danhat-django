from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify, truncatechars
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
        ordering = ["importance"]
    
    name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    importance = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Messages(models.Model):
    
    class Meta:
        verbose_name_plural = 'Messages'
        verbose_name = 'Messages'
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    phone_number = PhoneNumberField(unique = False, null = True, blank = True, region="US")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'



class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["importance"]

    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    importance = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name



class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Projects'
        verbose_name = 'Portfolio'
        ordering = ['importance']

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    link = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    importance = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        ordering = ["importance"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)
    importance = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'
        ordering = ['importance']

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    importance = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name