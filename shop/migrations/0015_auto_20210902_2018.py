# Generated by Django 3.2.6 on 2021-09-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_contactus_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='message',
            field=models.TextField(max_length=9000, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
