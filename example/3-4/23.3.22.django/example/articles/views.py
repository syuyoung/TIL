from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    foods = ['치킨', '삼겹살', '짜장면']
    pick = random.choice(foods)
    context = {
        'random' : pick
    }

    return render(request, 'articles/today_dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    data = request.GET.get('message')

    context = {
        'data': data,
    }
    return render(request, 'articles/catch.html', context)

def lotto_create(request):
    return render(request, 'articles/lotto_create.html')

def lotto(request):
    data = int(request.GET.get('message'))
    result = []
    for i in range(data):
        result.append(sorted(random.sample(range(1, 46), 6)))
    context = {
        'lottoNumber': result,
    }

    return render(request, 'articles/lotto.html', context)