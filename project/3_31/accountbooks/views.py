from django.shortcuts import render, redirect
from .models import AccountBook
# Create your views here.
def index(request):
    accountbook=AccountBook.objects.all()
    context={
        'accountbook' : accountbook,
    }
    return render(request, 'index.html',context)


def detail(request,account_book_pk):
    account=AccountBook.objects.get(pk=account_book_pk)
    context={
        'account':account,
    }
    return render(request, 'detail.html',context)


def new(request):
    return render(request, 'new.html')


def create(request):
    note=request.POST.get('note')
    description=request.POST.get('description')
    category=request.POST.get('category')
    amount=request.POST.get('amount')
    date=request.POST.get('date')
    accountbook=AccountBook(note=note, description=description, category=category, amount=amount, date=date)
    accountbook.save()

    # return render(request, 'create.html')
    return redirect("accountbooks:detail",accountbook.pk)


def delete(request,account_book_pk):
    accountBook = AccountBook.objects.get(pk=account_book_pk)
    accountBook.delete()
    return redirect("accountbooks:index")


def edit(request, account_book_pk):
    account=AccountBook.objects.get(pk=account_book_pk)
    context = {
        'account': account
    }
    return render(request, 'edit.html', context)

def update(request,account_book_pk):
    account=AccountBook.objects.get(pk=account_book_pk)
    account.note = request.POST.get('note')
    account.description = request.POST.get('description')
    account.category = request.POST.get('category')
    account.amount = request.POST.get('amount')
    account.date = request.POST.get('date')
    account.save()
    return redirect('accountbooks:detail',account_book_pk)

def copy1(request,account_book_pk):
    account = AccountBook.objects.get(pk=account_book_pk)
    accountbook = AccountBook()
    accountbook.note=account.note
    accountbook.description=account.description 
    accountbook.category=account.category 
    accountbook.amount=account.amount 
    accountbook.date=account.date
    accountbook.save()
    return redirect("accountbooks:index")
