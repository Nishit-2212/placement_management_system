# Generated by Django 4.2.4 on 2023-08-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placement_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
