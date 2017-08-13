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
    url(r'^collections/(?P<id>[\w-]+)/update/$', update_collection.as_view(), name="update_collections"),
    url(r'^collections/(?P<slug>[\w-]+)/delete/$', delete_collection.as_view(), name="delete_collection"),
    url(r'^collections/(?P<slug>[\w-]+)/$', collectionDetailView.as_view(), name="collection_detail"),


    #bookmarks
    url(r'^(?P<collection_id>[0-9]+)/create_bookmarks/$', create_bookmarks, name='create-bookmark'),
    url(r'^(?P<pk>[0-9]+)/delete_bookmark/$', delete_bookmark.as_view(),name="delete-bookmark"),
    #news
    url(r'^news/$',newsView, name="news"),
    # url(r'^news/$',newsListView.as_view(), name="news"),
    url(r'^news/(?P<slug>[\w-]+)/$', newsDetailView.as_view(), name="news_detail"),
    # url(r'^news/(?P<news>\w+)/$$',newsDetailView.as_view(), name="news"),

]