# Generated by Django 3.2.6 on 2021-09-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20210902_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=300, null=True),
        ),
    ]