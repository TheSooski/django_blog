from django.shortcuts import render, HttpResponse, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle


from django.contrib.auth.decorators import login_required, user_passes_test
def superuser_required(view_func=None, redirect_field_name=None, login_url=None):
    """
    Decorator that checks if the user is a superuser, redirecting
    to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator




def article_list(request):
    articles = Article.objects.all().order_by('data')
    return render(request, "articles/article_list.html", {"articles" : articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, "articles/article_detail.html", {"article":article})

@superuser_required(login_url="/accounts/login/")
#@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == "POST":
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:list")
    else:
        form = CreateArticle
    return render(request, "articles/article_create.html", {"form":form})