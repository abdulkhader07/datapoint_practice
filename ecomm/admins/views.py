from django.shortcuts import render

# Create your views here.
def fun(request):
    data = {
        'name':'adnan',
        'age':'20'
    }
    return render(request,'index.html',data)