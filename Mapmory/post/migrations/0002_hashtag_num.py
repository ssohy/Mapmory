# Generated by Django 4.2.4 on 2023-08-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='num',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
