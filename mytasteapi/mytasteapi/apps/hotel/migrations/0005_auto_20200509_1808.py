# Generated by Django 3.0.5 on 2020-05-09 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_hotelreservation_hotelroom_hotelroomtype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelreservation',
            old_name='type',
            new_name='hotel_room_type',
        ),
        migrations.RenameField(
            model_name='hotelroom',
            old_name='hotel_room',
            new_name='hotel_room_type',
        ),
    ]
