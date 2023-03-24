from django.shortcuts import render

# Create your views here.
def calculate(request, number1, number2):
    addition = number1+number2
    subtraction = number1-number2
    multiplication = number1*number2
    quotient = number1//number2

    context = {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication' : multiplication,
        'quotient' : quotient
    }
    return render(request, 'calculate/calculate.html', context)

def caculate2(request):
    return render(request, 'calculate/calculate2.html')