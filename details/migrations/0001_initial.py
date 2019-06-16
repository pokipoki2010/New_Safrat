# Generated by Django 2.1.2 on 2019-01-22 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateTimeField()),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time_date', models.DateTimeField()),
                ('end_time_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('end_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_station', to='details.Station')),
                ('start_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_station', to='details.Station')),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trip_train', to='details.Train')),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='train',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='train', to='details.Train'),
        ),
    ]