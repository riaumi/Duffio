from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day

def top(request):
    return render(request,'ani/top.html')

def profile(request):
    return render(request,'ani/profile.html')

def diary(request): # 日記一覧
    context = {
        'diary':Day.objects.all(), # models.pyにDayクラスの全てのデータをcontextに渡す
    }
    return render(request,'ani/diary.html',context)
    # render関数を使って、diary_htmlにcontextを渡す

def add(request): # 追加
    # 送信内容を元にフォームを作る。POSTじゃなければ空のフォームを作成。
    form = DayCreateForm(request.POST or None)

    # method==POSTとは送信ボタンが押されたとき。form.is_validは入力内容に問題が無い場合Trueになる。
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ani:diary')

    # 通常時のアクセスや入力内容に誤りがあれば、再度diary_form.htmlを表示
    context = {
        'form':form
    }
    return render(request, 'ani/diary_form.html', context)

def update(request, pk): # 更新
    # urlのpkを基に、Dayを取得（pkはidと同じ）
    # 更新記事の主キーが必要になるのでpkを引数に渡す
    day = get_object_or_404(Day, pk=pk)

    # formに取得したDayを紐づける
    form = DayCreateForm(request.POST or None, instance=day)

    # method=POST(送信ボタン押下)、でかつ、入力内容に問題がなければフォームを保存する。
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ani:diary')

    # 通常時のアクセスや入力内容に問題があった場合は最初のページを表示
    context = {
        'form':form
    }
    return render(request, 'ani/diary_form.html', context)

def delete(request, pk): # 削除
    # URLのPKを基に、Dayを取得（pkはidと同じ）
    day = get_object_or_404(Day, pk=pk)

    # method=POST(送信ボタン押下)
    if request.method == 'POST':
        day.delete() # 記事を削除
        return redirect('ani:diary')

    # 通常時のアクセス。または問題があった場合のアクセス。
    context = {
        'day':day
    }
    return render(request, 'ani/diary_delete.html', context)


def detail(request, pk): # 詳細
    # URLのPKを基に、Dayを取得
    day = get_object_or_404(Day, pk=pk)

    context = {
        'day':day
    }
    return render(request, 'ani/diary_detail.html', context)

def album(request):
    return render(request,'ani/album.html')

def fortune(request):
    return render(request,'ani/fortune.html')
    


