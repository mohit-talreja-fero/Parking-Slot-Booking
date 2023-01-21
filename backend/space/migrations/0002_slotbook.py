# Generated by Django 3.2 on 2023-01-04 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlotBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveIntegerField(default=0)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('payment', models.PositiveIntegerField(default=0)),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slot_bookings', to='space.slot')),
            ],
        ),
    ]
