# Generated by Django 4.1.1 on 2023-03-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patent', '0003_assignedto'),
    ]

    operations = [
        migrations.AddField(
            model_name='patentapplication',
            name='idf',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patentapplication',
            name='nda',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patentapplication',
            name='qua',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
    ]
