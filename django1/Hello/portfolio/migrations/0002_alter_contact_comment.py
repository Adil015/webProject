# Generated by Django 5.0.6 on 2024-06-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Comment',
            field=models.TextField(),
        ),
    ]
