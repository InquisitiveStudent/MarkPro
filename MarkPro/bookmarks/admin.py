from django.contrib import admin
from .models import newsboard, Collection, bookmarks
# Register your models here.
admin.site.register(newsboard)
admin.site.register(Collection)
admin.site.register(bookmarks)