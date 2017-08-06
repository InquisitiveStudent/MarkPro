from django.conf.urls import url
from bookmarks.views import (
    homeview,
    newsView,
    newsListView,
    newsDetailView,
)

urlpatterns= [
    url(r'^$', homeview , name="index"),
    url(r'^news/$',newsView, name="news"),
    url(r'^news/(?P<news>\w+)/$$',newsDetailView.as_view(), name="news"),
    url(r'^news/(?P<slug>\w+)/$',newsListView.as_view(), name="news"),

]