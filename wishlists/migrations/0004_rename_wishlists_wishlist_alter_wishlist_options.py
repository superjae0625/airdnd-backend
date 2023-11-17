# Generated by Django 4.2.4 on 2023-10-02 07:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0007_alter_room_city_alter_room_country_alter_room_rooms"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "experiences",
            "0004_alter_experience_category_alter_experience_host_and_more",
        ),
        (
            "wishlists",
            "0003_alter_wishlists_experiences_alter_wishlists_rooms_and_more",
        ),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Wishlists",
            new_name="Wishlist",
        ),
        migrations.AlterModelOptions(
            name="wishlist",
            options={},
        ),
    ]
