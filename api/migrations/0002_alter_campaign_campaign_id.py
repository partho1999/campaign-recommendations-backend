# Generated by Django 5.2.4 on 2025-07-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='campaign_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
