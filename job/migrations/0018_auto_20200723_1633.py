# Generated by Django 3.0.8 on 2020-07-23 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_auto_20200722_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='job.Job'),
        ),
    ]
