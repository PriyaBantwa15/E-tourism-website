# Generated by Django 4.0.3 on 2022-03-16 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etourism_app', '0004_delete_inquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('i_status', models.IntegerField()),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etourism_app.login')),
            ],
        ),
    ]
