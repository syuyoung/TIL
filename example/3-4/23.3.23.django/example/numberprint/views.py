from django.shortcuts import render

# Create your views here.
def number_print(request, number):
    context = {
        'number': number
    }
    return render(request, 'numberprint/number_print.html', context)

def number_print2(request):
    return render(request, 'numberprint/number_print2.html')