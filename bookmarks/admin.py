from django.contrib import admin
from .models import Newsboard, Collection, Bookmarks
# Register your models here.
admin.site.register(Newsboard)
admin.site.register(Collection)
admin.site.register(Bookmarks)