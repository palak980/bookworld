# Generated by Django 3.2.14 on 2022-07-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Testapp', '0002_auto_20220704_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
