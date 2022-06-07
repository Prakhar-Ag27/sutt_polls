# Generated by Django 4.0.4 on 2022-06-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fnapp', '0010_through_time_of_issue_int_alter_item_unique_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='through',
            name='current_issued',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='unique_code',
            field=models.IntegerField(default=27219745, editable=False),
        ),
        migrations.AlterField(
            model_name='through',
            name='qty_issued',
            field=models.IntegerField(default=0),
        ),
    ]