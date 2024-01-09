# Generated by Django 5.0.1 on 2024-01-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_category', models.CharField(max_length=60)),
                ('organization_name', models.CharField(max_length=60)),
                ('adderss_1', models.CharField(max_length=140)),
                ('adderss_2', models.CharField(max_length=140)),
                ('state', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('zipcode', models.IntegerField()),
                ('phone_number', models.CharField(max_length=60)),
                ('fax_number', models.CharField(max_length=60)),
                ('website', models.CharField(max_length=250)),
                ('twitter', models.CharField(max_length=200)),
            ],
        ),
    ]