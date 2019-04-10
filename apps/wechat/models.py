from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Xf_list(models.Model):
    openid = models.CharField(max_length=28, verbose_name=u'用户唯一号码')
    nickname = models.CharField(max_length=50, verbose_name=u'用户昵称')
    sex = models.IntegerField(default=3, verbose_name=u'性别')
    province = models.CharField(max_length=20, verbose_name=u'省')
    country = models.CharField(max_length=20, verbose_name=u'国家')
    city = models.CharField(max_length=20, verbose_name=u'城市')
    headimgurl = models.URLField(default='', verbose_name=u'图像')
    begin_time = models.DateTimeField(verbose_name=u'开始时间', default=timezone.now)
    end_time = models.DateTimeField(verbose_name=u'结束时间', default=timezone.now)
    stauts = models.IntegerField(default=1, verbose_name=u'状态')

    def __unicode__(self):
        return self.nickname

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = u'用户信息'


class Dev_token(models.Model):
    tid = models.CharField(max_length=2)
    device_name = models.CharField(max_length=50)
    apiid = models.CharField(max_length=18, default='bl397233b7de02c055')
    apikey = models.CharField(max_length=32, default='da5cbd210dbd9e994a9fdf5731aaae51')
    expires_in = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'keyM'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.device_name