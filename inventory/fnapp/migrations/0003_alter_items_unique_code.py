# Generated by Django 4.0.4 on 2022-05-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fnapp', '0002_rename_no_of_issued_items_items_no_of_items_issued_out_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='unique_code',
            field=models.IntegerField(default=86711740, editable=False, max_length=100),
        ),
    ]
