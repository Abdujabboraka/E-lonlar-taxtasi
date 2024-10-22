# Generated by Django 5.1.1 on 2024-10-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_profile_delete_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatar'),
        ),
    ]
