# Generated by Django 3.0.5 on 2020-05-07 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200427_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userlovedhotel',
            options={'verbose_name': '用户收藏/去过的酒店', 'verbose_name_plural': '用户收藏/去过的酒店'},
        ),
        migrations.AlterModelOptions(
            name='userlovedscene',
            options={'verbose_name': '用户收藏/去过的景点', 'verbose_name_plural': '用户收藏/去过的景点'},
        ),
    ]