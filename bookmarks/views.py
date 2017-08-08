from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView,DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Newsboard, Collection, Bookmarks
from .forms import LoginForm, CollectionForm, NewsboardForm, BookmarkForm
from django.http import HttpResponseRedirect

def homeview(request):
    #HomeTemplateView
    if not request.user.is_authenticated():
        template_name = 'bookmarks/home_visitor.html'
    else:
        template_name = 'bookmarks/home.html'
    story = Newsboard.objects.all().order_by('-timestamp')
    context = {
        "newsboard": story
    }
    return render(request, template_name, context)

def newsView(request):
    template_name = "bookmarks/news.html"
    story = Newsboard.objects.all().order_by('-timestamp')
    context = {
        "newsboard": story
    }
    return render(request, template_name, context)

class newsListView(ListView):
    """
        Same as newsView(request)
        ListView to display news with filter

    """
    queryset= Newsboard.objects.all()
    template_name = "bookmarks/news.html"
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset=Newsboard.objects.filter(
                Q(topic__iexact=slug) |
                Q(topic__icontains=slug)
            )
        else:
            queryset=Newsboard.objects.all()
        return queryset

class newsDetailView(DetailView):

    queryset= Newsboard.objects.all()
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
    #     obj=get_object_or_404(Newsboard, id=news_id)
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
                story = Newsboard.objects.all().order_by('-timestamp')
                context = {
                    "Newsboard": story
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
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
                #does not change url
                # return render(request, 'bookmarks/home.html', { 'user': request.user } )

    return render(request, 'bookmarks/login/register.html', {'form': form})



def collectionView(request):
    if not request.user.is_authenticated():
        return render(request, 'bookmarks/login/login.html')
    else:
        collections = Collection.objects.filter(user=request.user)
        return render(request, 'bookmarks/collections.html', {'collections': collections})

class collectionDetailView(DetailView):
    template_name = 'bookmarks/collections_detail.html'
    queryset= Collection.objects.all()




def create_collection(request):
    if not request.user.is_authenticated():
        return request(request,'bookmarks/login/login.html',{})
    else:
        form = CollectionForm(request.POST or None)
        if form.is_valid():
            collection=form.save(commit=False)
            collection.user= request.user
            collection.save()

            return render(request, 'bookmarks/collections.html', {'collections': collection})
    context={
        'form': form
    }
    return render(request, 'bookmarks/create_collection.html',context)



class delete_collection(DeleteView):
    model = Collection
    success_url = reverse_lazy('bookmarks:collections')
    """
    Function based delete
    def delete_collection(request, collection_id):
    collection = Collection.objects.get(pk=album_id)
    collection.delete()
    collection = Collection.objects.filter(user=request.user)
    return render(request, 'bookmarks/index.html', {'collection':s collection})
    """
    # from django.http import Http404
    # def get_object(self, queryset=None):
    #     """ Hook to ensure object is owned by request.user. """
    #     obj = super(collection_delete, self).get_object()
    #     if not obj.owner == self.request.user:
    #         raise Http404
    #     return obj


def create_bookmarks(request, collection_id):
    if not request.user.is_authenticated():
        return render(request,'bookmarks/login/login.html')
    else:
        form = BookmarkForm(request.POST or None)
        collections =get_object_or_404(Collection, pk = collection_id )

        if form.is_valid():
            """
            Alternative to get object from user. 
            >>> user=request.user
            >>> collections_links= user.objects.get(id= collection_id)
            to
            >>> collections_links = User.objects.get(id= request.user.id)
            """
            """
                Manager isn't accessible via `Model` instances
                Solution:
                    Reverse related object lookup.

            """

            collections_links = collections.bookmarks_set.all()


            for s in collections_links:
                if s.bookmarks_title == form.cleaned_data.get('bookmarks_title'):
                    context={
                        'form': form,
                        'collections': collections,
                        'error_message': "Ops.. There's a title name similar to this. Please use other title to avoid conflict"

                    }
                    return render(request, 'bookmarks/create_bookmarks.html', context)
            links = form.save(commit=False)
            links.list_bookmark = collections
            #Match the Foreign Key
            links.save()
            return render(request, 'bookmarks/collections_detail.html',{ 'collections': collections })

    context= {
        'collections': collections,
        'form': form

    }
    return render(request, 'bookmarks/create_bookmark.html', context)

