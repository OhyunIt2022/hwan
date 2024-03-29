from sre_parse import Verbose
from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(verbose_name='북마크 제목',max_length=50)
    url = models.URLField(verbose_name='URL')
    memo = models.TextField(verbose_name='메모')