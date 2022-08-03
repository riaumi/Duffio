from django import forms
from .models import Day

class DayCreateForm(forms.ModelForm):
    class Meta:
        model = Day
        fields='__all__' # 全てのデータを渡す

# 入力欄を作成するにあたり、HTMLファイルにFormというものを構成する必要がある。
# そのFormに対して、どんなデータを渡すのかを定義するのがこのforms.py