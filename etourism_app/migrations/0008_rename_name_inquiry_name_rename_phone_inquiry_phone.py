# Generated by Django 4.0.3 on 2022-03-16 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etourism_app', '0007_alter_feedback_ratting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inquiry',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='inquiry',
            old_name='Phone',
            new_name='phone',
        ),
    ]