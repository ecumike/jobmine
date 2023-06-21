# Generated by Django 4.2.2 on 2023-06-21 18:57

import applications.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('applied_date', models.DateField(default=applications.models.getToday)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('open', 'Waiting'), ('declined', 'Declined')], default='open', max_length=10)),
                ('contact_names', models.TextField(blank=True)),
                ('contact_emails', models.TextField(blank=True)),
                ('initial_screen', models.BooleanField(default=False)),
                ('round_1', models.BooleanField(default=False)),
                ('round_2', models.BooleanField(default=False)),
                ('round_3', models.BooleanField(default=False)),
                ('round_4', models.BooleanField(default=False)),
                ('round_5', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='job_posting_company', to='applications.company')),
            ],
            options={
                'ordering': ['company', 'title'],
            },
        ),
    ]
