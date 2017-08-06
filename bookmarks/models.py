from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator


class Newsboard(models.Model):
    title = models.CharField(max_length = 255)
    topic = models.CharField(max_length= 255)
    description = models.TextField()
    timestamp= models.DateTimeField(auto_now=False, auto_now_add=True)
    updated= models.DateTimeField(auto_now=True, auto_now_add=False)
    slug= models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.title

def rl_pre_save_receiver(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Newsboard)

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list_title=models.CharField(max_length=200)
    list_type=models.CharField(max_length=200)
    list_description=models.TextField()
    timestamp= models.DateTimeField(auto_now=False, auto_now_add=True)
    updated= models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.list_title

class Bookmarks(models.Model):

    list_bookmark=models.ForeignKey(Collection, on_delete=models.CASCADE)
    bookmarks_title= models.CharField(max_length=255)
    bookmarks_links= models.CharField(max_length=255)
    bookmarks_description= models.TextField()

    def __str__(self):
        return self.bookmarks_title


"""
Add timestamp and modified time.
Source over here
https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add
---------------------------------------
I would recommend not using auto_now or auto_now_add and
instead define your own save() method to make sure that created is only updated if id is not set 
(such as when the item is first created), 
and have it update modified every time the item is saved.
from django.utils import timezone

class User(models.Model):
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)

"""