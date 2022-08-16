# Generated by Django 4.0.6 on 2022-08-14 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('distributor', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('evaluation', models.CharField(max_length=100)),
            ],
        ),
    ]