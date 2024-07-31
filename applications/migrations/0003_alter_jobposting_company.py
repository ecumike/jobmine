# Generated by Django 4.2.4 on 2024-07-31 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("applications", "0002_jobposting_is_archived"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobposting",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="job_posting_company",
                to="applications.company",
            ),
        ),
    ]
