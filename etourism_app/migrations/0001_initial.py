# Generated by Django 4.0.3 on 2022-03-05 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covid_cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_cases', models.CharField(max_length=100)),
                ('total_cases', models.CharField(max_length=100)),
                ('current_cases', models.CharField(max_length=100)),
                ('total_death', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('schemes', models.TextField()),
                ('prices', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('i_status', models.IntegerField()),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etourism_app.login')),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_cases', models.CharField(max_length=30)),
                ('hotel_name', models.CharField(max_length=100)),
                ('address_link', models.TextField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=50)),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etourism_app.package')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('ratting', models.IntegerField()),
                ('comment', models.TextField()),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etourism_app.login')),
            ],
        ),
        migrations.CreateModel(
            name='covid_vaccinated_certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.FileField(upload_to='certificate')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etourism_app.login')),
            ],
        ),
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_status', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etourism_app.hotel')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etourism_app.login')),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etourism_app.package')),
            ],
        ),
    ]
