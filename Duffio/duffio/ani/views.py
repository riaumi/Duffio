from django.shortcuts import render,redirect
from .forms import DayCreateForm

def top(request):
    return render(request,'ani/top.html')

def profile(request):
    return render(request,'ani/profile.html')

def diary(request):
    return render(request,'ani/diary.html')

def add(request):
    # 送信内容をもとにフォームを作る。POSTじゃなければ空のフォーム
    form = DayCreateForm(request.POST or None)

    # method=POST、つまり送信ボタンを押下時、入力内容に問題がなければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ani:diary')
    
    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form':form
    }
    return render(request,'ani/diary_form.html',context)


def album(request):
    return render(request,'ani/album.html')

def fortune(request):
    return render(request,'ani/fortune.html')
    


