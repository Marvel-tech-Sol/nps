# Generated by Django 4.1.1 on 2023-04-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patent', '0006_drawingstatus_assignto_drawingstatus_duedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawingstatus',
            name='duedate',
            field=models.DateField(max_length=20, null=True),
        ),
    ]
