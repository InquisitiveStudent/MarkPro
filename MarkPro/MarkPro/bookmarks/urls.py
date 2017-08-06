from django.conf.urls import url
from .views import *

urlpatterns= [
    url(r'^$', homeview , name="index"),
    url(r'^login/$', loginView , name="login_user"),
    url(r'^logout_user/$', logoutView, name='logout_user'),
    url(r'^register/$', registerView , name="register"),

    url(r'^collections/$', collectionView , name="collections"),
    url(r'^news/$',newsView, name="news"),
    # url(r'^news/$',newsListView.as_view(), name="news"),

    url(r'^news/(?P<slug>[\w-]+)/$', newsDetailView.as_view(), name="news"),
    # url(r'^news/(?P<news>\w+)/$$',newsDetailView.as_view(), name="news"),




]