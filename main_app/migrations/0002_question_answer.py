# Generated by Django 4.0.6 on 2022-07-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
