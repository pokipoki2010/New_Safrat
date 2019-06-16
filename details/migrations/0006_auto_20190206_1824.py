# Generated by Django 2.1.2 on 2019-02-06 18:24

import details.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0005_auto_20190206_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='first_name',
            field=models.CharField(max_length=100, null=True, validators=[details.models.validate_string]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='last_name',
            field=models.CharField(max_length=100, null=True, validators=[details.models.validate_string]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='middle_name',
            field=models.CharField(max_length=100, null=True, validators=[details.models.validate_string]),
        ),
    ]
