# Generated by Django 4.2.2 on 2023-06-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_jobposting_declined_date_alter_jobposting_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='initial_contact_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
