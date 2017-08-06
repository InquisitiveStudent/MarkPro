from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from .models import newsboard, Collection, bookmarks


def homeview(request):
    #HomeTemplateView
    template_name = 'bookmarks/home.html'
    story = newsboard.objects.all()
    context = {
        "newsboard": story
    }
    return render(request, template_name, context)

def newsView(request):
    template_name = "bookmarks/news.html"
    story = newsboard.objects.all()
    context = {
        "newsboard": story
    }
    return render(request, template_name, context)

class newsListView(ListView):
    """
        ListView to display news with filter

    """
    qs= newsboard.objects.all()
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            qs=newsboard.objects.filter(
                Q(topic__iexact=slug) |
                Q(topic__icontains=slug)
            )
        else:
            qs=newsboard.objects.all()
        return qs

class newsDetailView(DetailView):
    queryset= newsboard.objects.all()
    def get_context_data(self, *args, **kwargs):
        print(self.kwargs)
        #get the id
        context= super(newsDetailView,self).get_context_data(*args, **kwargs)
        print(context)
        # it returns the object details
        return context

    def get_object(self, *args, **kwargs):
        """
            This function is to change the urls.py as news_id
            pk  >  news_id
            url(r'^news/(?P<news_id>\w+)/$$', newsDetailView.as_view(), name="news"),
            if not will get AttributeError. Must be pk or slug.
            This function is not necessary if you stay as pk or slug.
        """
        news_id= self.kwargs.get('news_id')
        obj=get_object_or_404(newsboard, id=news_id)
        return obj
