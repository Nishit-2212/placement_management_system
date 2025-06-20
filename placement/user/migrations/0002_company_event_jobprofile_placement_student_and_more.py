# Generated by Django 4.2.4 on 2023-08-16 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('required_skills', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.company')),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placement_date', models.DateTimeField(auto_now_add=True)),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.jobprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('resume', models.FileField(upload_to='resumes/')),
                ('skills', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='users_data',
        ),
        migrations.AddField(
            model_name='placement',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student'),
        ),
    ]
