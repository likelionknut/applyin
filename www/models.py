from django.db import models


# Create your models here.

class Job(models.Model):
    class Meta:
        verbose_name = '채용 정보'
        verbose_name_plural = '채용 정보'

    company = models.CharField(max_length=50, verbose_name='기업명')
    date_created = models.DateField(auto_now_add=True,  verbose_name='공고일')
    date_deadline = models.DateField(auto_now_add=False,  verbose_name='마감일')
    summary = models.TextField(max_length=10000, null=True, blank=False, verbose_name='요약')
    logo = models.ImageField(upload_to='images/logo', null=True, blank=True, verbose_name='기업 로고')
    background = models.ImageField(upload_to='images/background', null=True, blank=True, verbose_name='배경 이미지')


class Application(models.Model):
    class Meta:
        verbose_name = '지원서'
        verbose_name_plural = '지원서'

    name = models.CharField(max_length=50, verbose_name='이름')
    email = models.EmailField(max_length=50, verbose_name='이메일')
    phone = models.CharField(max_length=30, verbose_name='연락처')
    address = models.CharField(max_length=200, verbose_name='주소')

    # 경력
    prev_company = models.CharField(max_length=50, verbose_name='회사명')
    prev_department = models.CharField(max_length=50, verbose_name='부서명')
    prev_date_join = models.CharField(max_length=50, verbose_name='입사일')
    prev_date_leave = models.CharField(max_length=50, verbose_name='퇴사일')
    prev_position = models.CharField(max_length=50, verbose_name='직급/직책')
    prev_location = models.CharField(max_length=50, verbose_name='지역')

# class Career(models.Model):
#     pass
