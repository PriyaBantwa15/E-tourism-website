# Generated by Django 4.0.3 on 2022-04-06 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etourism_app', '0012_alter_place_detail_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place_detail',
            old_name='image',
            new_name='video',
        ),
    ]