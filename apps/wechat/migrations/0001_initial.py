# Generated by Django 2.2 on 2019-04-10 16:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dev_token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(max_length=2)),
                ('device_name', models.CharField(max_length=50)),
                ('apiid', models.CharField(default='bl397233b7de02c055', max_length=18)),
                ('apikey', models.CharField(default='da5cbd210dbd9e994a9fdf5731aaae51', max_length=32)),
                ('expires_in', models.CharField(max_length=100)),
                ('access_token', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'keyM',
                'verbose_name_plural': 'keyM',
            },
        ),
        migrations.CreateModel(
            name='Xf_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=28, verbose_name='用户唯一号码')),
                ('nickname', models.CharField(max_length=50, verbose_name='用户昵称')),
                ('sex', models.IntegerField(default=3, verbose_name='性别')),
                ('province', models.CharField(max_length=20, verbose_name='省')),
                ('country', models.CharField(max_length=20, verbose_name='国家')),
                ('city', models.CharField(max_length=20, verbose_name='城市')),
                ('headimgurl', models.URLField(default='', verbose_name='图像')),
                ('begin_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='结束时间')),
                ('stauts', models.IntegerField(default=1, verbose_name='状态')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]
