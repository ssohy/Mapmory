from django.db import models
from django.utils import timezone

#해시태그 모델
class Hashtag(models.Model):
    name = modles.CharField(max_length=50)

    def __str__(self):
        return self.name

#글 작성
class Post(models.Model):
    title = models.CharField(max_length=60, verbose_name='제목')
    contents = models.TextField(verbose_name='글쓰기')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashtag = models.ManyToManyField(Hashtag)
    datetime = models.DateTimeField(auto_now=True)
