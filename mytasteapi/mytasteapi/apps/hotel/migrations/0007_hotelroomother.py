# Generated by Django 3.0.5 on 2020-05-09 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20200509_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRoomOther',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='空闲房间数')),
                ('day', models.DateField(verbose_name='日期')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Hotel', verbose_name='酒店')),
                ('hotel_room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.HotelRoomType', verbose_name='房型')),
            ],
            options={
                'verbose_name': '酒店房间other',
                'verbose_name_plural': '酒店房间other',
                'db_table': 'mt_hotel_room_other',
            },
        ),
    ]