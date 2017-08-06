from django.conf.urls import url
from .views import *

urlpatterns= [
    url(r'^$', homeview , name="index"),
    url(r'^login/$', loginView , name="login_user"),
    url(r'^logout_user/$', logoutView, name='logout_user'),
    url(r'^register/$', registerView , name="register"),

    #collections
    url(r'^collections/$', collectionView , name="collections"),
    url(r'^collections/create/$', create_collection, name="create_collections"),
    url(r'^(?P<collection_id>[0-9]+)/create_bookmarks/$', create_bookmarks, name='create_song'),
    url(r'^(?P<collection_id>[0-9]+)/delete/$', delete_collection, name="delete_collection"),
    url(r'^collections/(?P<slug>[\w-]+)/$', collectionDetailView.as_view(), name="coll_detail"),

    #news
    url(r'^news/$',newsView, name="news"),
    # url(r'^news/$',newsListView.as_view(), name="news"),
    url(r'^news/(?P<slug>[\w-]+)/$', newsDetailView.as_view(), name="news_detail"),
    # url(r'^news/(?P<news>\w+)/$$',newsDetailView.as_view(), name="news"),

]