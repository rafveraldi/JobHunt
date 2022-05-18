# Generated by Django 4.0.3 on 2022-03-23 17:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, null=True)),
                ('date_applied', models.DateField(default=datetime.date.today, verbose_name='Date Applied')),
                ('stage', models.CharField(choices=[('JOBAPPLIED', 'Job Applied'), ('HRCALL', 'HR call'), ('FSTINT', 'First Interview'), ('SNDINT', 'Second Interview'), ('TRDINT', 'Third Interview'), ('JOBOFFER', 'Job Offer'), ('DENIED', 'Denied')], default='JOBAPPLIED', max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_applied'],
            },
        ),
    ]