# Generated by Django 4.2.4 on 2023-09-29 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0006_alter_room_amenities_alter_room_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="city",
            field=models.CharField(default="서울", max_length=80),
        ),
        migrations.AlterField(
            model_name="room",
            name="country",
            field=models.CharField(default="한국", max_length=50),
        ),
        migrations.AlterField(
            model_name="room",
            name="rooms",
            field=models.PositiveIntegerField(),
        ),
    ]