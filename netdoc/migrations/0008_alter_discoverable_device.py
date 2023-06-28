# Generated by Django 4.1.8 on 2023-06-26 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netdoc', '0007_discoverylog_supported'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discoverable',
            name='device',
            field=models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.device'),
        ),
    ]