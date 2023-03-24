from django.shortcuts import render, HttpResponse, redirect
from .models import Sell
from django.contrib.auth.decorators import login_required
from .forms import CreateSell


# def article_list(request):
#     articles = Article.objects.all().order_by('data')
#     return render(request, "articles/article_list.html", {"articles" : articles})

def sell_detail(request, slug):
    sell = Sell.objects.get(slug=slug)
    return render(request, "sell/sell_detail.html", {"sell":sell})

@login_required(login_url="/accounts/login/")
def sell_create(request):
    if request.method == "POST":
        form = CreateSell(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.seller = request.user
            #instance.book_slug = slug
            instance.save()
            return redirect("articles:list")
    else:
        form = CreateSell()
    return render(request, "sell/sell_create.html", {"form":form})
