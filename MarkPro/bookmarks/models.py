from django.db import models
from django.contrib.auth.models import User


class newsboard(models.Model):
    title = models.CharField(max_length = 255)
    topic = models.CharField(max_length= 255)
    description = models.TextField()
    timestamp= models.DateTimeField(auto_now=False, auto_now_add=True)
    updated= models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title



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

class bookmarks(models.Model):

    list_bookmark=models.ForeignKey(Collection, on_delete=models.CASCADE)
    bookmarks_title= models.CharField(max_length=200)
    bookmarks_links= models.CharField(max_length=2000)
    bookmarks_description= models.CharField(max_length=2000)

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