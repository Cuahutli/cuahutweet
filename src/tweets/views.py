from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from django.forms.utils import ErrorList
from django import forms
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin

# Create your views here.

# Create
## Whitout mixins Class declaration
##class TweetCreateView(CreateView):
class TweetCreateView(FormUserNeededMixin, CreateView):
    #queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/'

    #if whithout mixins class then use this functions (is the same in mixins)
    # def form_valid(self, form):
    #     if self.request.user.is_authenticated():
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["el usuario debe estar logueado para continuar"])
    #         return self.form_invalid(form)


# is same the TweetCreateView
# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#     context = {
#         "form": form
#     }
#     return render(request, 'tweets/create_view.html', context)
# Update

# Delete

# List/Search

# Retrieve



class TweetDetailView(DetailView):
    #template_name = 'tweets/detail_view.html'
    queryset = Tweet.objects.all()

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        print(pk)
        obj = get_object_or_404(Tweet, pk=pk)
        return obj

class TweetListView(ListView):
    #template_name = 'tweets/list_view.html'
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        #context["another_list"] = Tweet.objects.all()
        #print(context)
        return context


def tweet_detail_view(request, pk=1):  # pk == id
    #obj = Tweet.objects.get(pk=pk) # GET from database
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object": obj
    }
    return render(request, 'tweets/detail_view.html', context)