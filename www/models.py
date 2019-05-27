from django.db import models


# Create your models here.

class Job(models.Model):
    class Meta:
        verbose_name = '채용 정보'
        verbose_name_plural = '채용 정보'

    company = models.CharField(max_length=50, verbose_name='기업명')
    date_created = models.DateField(auto_now_add=True, verbose_name='공고일')
    date_deadline = models.DateField(auto_now_add=False, verbose_name='마감일')
    summary = models.TextField(max_length=10000, null=True, blank=False, verbose_name='요약')
    logo = models.ImageField(upload_to='images/logo', null=True, blank=True, verbose_name='기업 로고')
    background = models.ImageField(upload_to='images/background', null=True, blank=True, verbose_name='배경 이미지')
