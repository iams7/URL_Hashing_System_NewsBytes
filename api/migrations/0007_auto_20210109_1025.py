# Generated by Django 3.1.5 on 2021-01-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210109_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utmparameter',
            name='campaign_hashed_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='utmparameter',
            name='campaign_url',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
