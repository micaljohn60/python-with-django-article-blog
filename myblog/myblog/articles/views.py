from django.shortcuts import render
from django.shortcuts import redirect
from .models import Article
from django.http import HttpResponse
from .import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html',{'articles' : articles})

@login_required()
def article_detail(request,slug):
    # return HttpResponse(slug)
    articles = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article': articles})

@login_required()
def create_post(request):    
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            #save articel to DB
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request,'articles/createpost.html',{'forms':form})