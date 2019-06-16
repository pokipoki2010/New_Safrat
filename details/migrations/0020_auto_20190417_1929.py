# Generated by Django 2.1.7 on 2019-04-17 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0019_auto_20190417_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='number_of_tickets',
        ),
        migrations.AddField(
            model_name='passenger',
            name='number_of_tickets',
            field=models.ForeignKey(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')], default=1, on_delete=django.db.models.deletion.CASCADE, to='details.Ticket'),
        ),
    ]
