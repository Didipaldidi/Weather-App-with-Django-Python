# Generated by Django 4.2.1 on 2023-07-13 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_city_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherForecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('low_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('high_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.city')),
            ],
        ),
    ]