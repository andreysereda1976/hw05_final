# Generated by Django 2.2.9 on 2020-05-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200522_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
