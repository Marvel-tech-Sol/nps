# Generated by Django 4.1.1 on 2023-06-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patent', '0012_remove_ferstatus_date_ferstatus_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftingstatus',
            name='qc',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='drawingstatus',
            name='qc',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='noveltystatus',
            name='qc',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='noveltystatus',
            name='rating',
            field=models.CharField(max_length=20),
        ),
    ]