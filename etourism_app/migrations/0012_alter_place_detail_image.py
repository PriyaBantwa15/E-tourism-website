# Generated by Django 4.0.3 on 2022-04-04 10:46

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('etourism_app', '0011_alter_place_detail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place_detail',
            name='image',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
