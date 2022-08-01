from django.shortcuts import render

def top(request):
    return render(request,'ani/top.html')

def profile(request):
    return render(request,'ani/profile.html')

def diary(request):
    return render(request,'ani/diary.html')

def album(request):
    return render(request,'ani/album.html')

def fortune(request):
    return render(request,'ani/fortune.html')
    


