# Generated by Django 5.1.1 on 2024-10-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_announcement_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='announcement',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
