# Generated by Django 4.1 on 2022-08-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_anti_d', '0002_localgovernments_alter_disastername_mode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localgovernments',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
