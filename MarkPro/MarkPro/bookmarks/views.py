from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from .models import newsboard, Collection, bookmarks
from .forms import LoginForm, CollectionForm, NewsboardForm, BookmarkForm

def homeview(request):
    #HomeTemplateView
    if not request.user.is_authenticated():
        template_name = 'bookmarks/home_visitor.html'
    else:
        template_name = 'bookmarks/home.html'
    story = newsboard.objects.all().order_by('-timestamp')
    context = {
        "newsboard": story
    }
    return render(request, template_name, context)

def newsView(request):
    template_name = "bookmarks/news.html"
    story = newsboard.objects.all().order_by('-timestamp')
    context = {
        "newsboard": story
    }
    return render(request, template_name, context)

class newsListView(ListView):
    """
        Same as newsView(request)
        ListView to display news with filter

    """
    queryset= newsboard.objects.all()
    template_name = "bookmarks/news.html"
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset=newsboard.objects.filter(
                Q(topic__iexact=slug) |
                Q(topic__icontains=slug)
            )
        else:
            queryset=newsboard.objects.all()
        return queryset

class newsDetailView(DetailView):

    queryset= newsboard.objects.all()


    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     #get the id
    #     context= super(newsDetailView,self).get_context_data(*args, **kwargs)
    #     print(context)
    #     # it returns the object details
    #     return context

    # def get_object(self, *args, **kwargs):
    #     """
    #         This function is to change the urls.py as news_id
    #         pk  >  news_id
    #         url(r'^news/(?P<news_id>\w+)/$$', newsDetailView.as_view(), name="news"),
    #         if not will get AttributeError. Must be pk or slug.
    #         This function is not necessary if you stay as pk or slug.
    #     """
    #     news_id= self.kwargs.get('news_id')
    #     obj=get_object_or_404(newsboard, id=news_id)
    #     return obj


def loginView(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                if not request.user.is_authenticated():
                    template_name = 'bookmarks/home_visitor.html'
                else:
                    template_name = 'bookmarks/home.html'
                story = newsboard.objects.all().order_by('-timestamp')
                context = {
                    "newsboard": story
                }
                return render(request, template_name, context)

            else:
                return render(request, 'bookmarks/login/login.html',{'error_message': 'Your account has been disabled'})
        else:
            return render(request,'bookmarks/login/login.html', {'error_message': 'Invalid Login'})
    return render(request, 'bookmarks/login/login.html')

def logoutView(request):
    logout(request)
    form = LoginForm(request.POST or None)
    return render(request, 'bookmarks/login/login.html',{'form': form })

def registerView(request):
    pass


def collectionView(request):
    if not request.user.is_authenticated():
        return render(request, 'bookmarks/login/login.html')
    else:
        collections = Collection.objects.filter(user=request.user)
        return render(request, 'bookmarks/home.html', {'collections': collections})