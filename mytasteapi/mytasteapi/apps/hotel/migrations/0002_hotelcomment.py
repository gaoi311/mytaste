# Generated by Django 3.0.5 on 2020-04-25 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024, verbose_name='评论内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Hotel', verbose_name='酒店')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '酒店评论',
                'verbose_name_plural': '酒店评论',
                'db_table': 'mt_hotel_comment',
            },
        ),
    ]