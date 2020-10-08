# Generated by Django 3.0.8 on 2020-07-21 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_apply_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='cover',
            new_name='cover_letter',
        ),
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='job.Job'),
        ),
    ]