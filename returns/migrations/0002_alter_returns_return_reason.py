# Generated by Django 3.2 on 2022-09-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('returns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returns',
            name='return_reason',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
