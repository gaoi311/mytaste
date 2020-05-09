# Generated by Django 3.0.5 on 2020-05-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_auto_20200509_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelreservation',
            name='hotel_room_type',
        ),
        migrations.AddField(
            model_name='hotelreservation',
            name='type',
            field=models.IntegerField(choices=[(1, '标准间'), (2, '单人间'), (3, '双人间'), (4, '三人间'), (5, '大床房'), (6, '亲子间')], default=1, verbose_name='房间类型'),
            preserve_default=False,
        ),
    ]