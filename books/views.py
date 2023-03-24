from django.shortcuts import render, HttpResponse, redirect
from .models import Books
from django.contrib.auth.decorators import login_required
from .forms import CreateBook

def books_list(request):
    books = Books.objects.all().order_by('title')
    return render(request, "books/books_list.html", {"books" : books})

def books_detail(request, slug):
    books = Books.objects.get(slug=slug)
    return render(request, "books/books_detail.html", {"books" : books})


@login_required(login_url="/accounts/login/")
def books_create(request):
    if request.method == "POST":
        form = CreateBook(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("books:list")
    else:
        form = CreateBook
    return render(request, "books/books_create.html", {"form":form})
