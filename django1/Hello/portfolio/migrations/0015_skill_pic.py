# Generated by Django 5.0.6 on 2024-07-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_rename_i_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='assets/c++.png/'),
        ),
    ]
