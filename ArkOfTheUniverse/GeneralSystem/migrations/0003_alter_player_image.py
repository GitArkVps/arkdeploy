# Generated by Django 4.1.3 on 2022-11-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeneralSystem', '0002_player_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='player/picture/'),
        ),
    ]