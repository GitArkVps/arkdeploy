# Generated by Django 4.1.3 on 2022-11-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElementSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='element/representation/'),
        ),
        migrations.AlterField(
            model_name='rarity',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='element/rarity/'),
        ),
    ]