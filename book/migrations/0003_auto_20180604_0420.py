# Generated by Django 2.0.3 on 2018-06-04 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20180604_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
