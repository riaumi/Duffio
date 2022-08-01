from django.shortcuts import render

def index(request):
    context = {

    }
    return render(request,'ani/index.html',context)
    


