# Generated by Django 4.2 on 2023-10-26 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='profile-picture.png', upload_to='profile_images'),
        ),
    ]