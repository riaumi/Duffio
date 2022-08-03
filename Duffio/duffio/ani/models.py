from django.db import models
from django.utils import timezone

class Day(models.Model):
    # models.pyで明示的に主キーを設定しなかった場合、idという主キーが自動でセットされる
    title = models.CharField('タイトル',max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)


