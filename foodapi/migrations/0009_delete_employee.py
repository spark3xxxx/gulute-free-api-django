# Generated by Django 4.0.6 on 2022-08-27 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapi', '0008_rename_user_id_wishlist_user_uid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
