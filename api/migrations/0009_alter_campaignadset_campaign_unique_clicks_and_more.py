# Generated by Django 5.2.4 on 2025-07-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_campaignadset_delete_campaignad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignadset',
            name='campaign_unique_clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='cluster',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='conversion_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='conversions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='cost',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='cr',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='day',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='lp_clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='lp_ctr',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='potential_impact',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='profit',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='profit_margin',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='recommendation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='revenue',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='revenue_to_cost_ratio',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='roi_confirmed',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='sub_id_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='sub_id_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='sub_id_5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='campaignadset',
            name='sub_id_6',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
