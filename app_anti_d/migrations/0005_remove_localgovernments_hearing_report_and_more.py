# Generated by Django 4.1 on 2022-08-16 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_anti_d', '0004_hearingreportsfromlocalgovernment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localgovernments',
            name='hearing_report',
        ),
        migrations.AddField(
            model_name='hearingreportsfromlocalgovernment',
            name='heard_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_anti_d.localgovernments'),
        ),
    ]
