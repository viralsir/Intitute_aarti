# Generated by Django 3.1.7 on 2021-04-01 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_master',
            name='fees',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
