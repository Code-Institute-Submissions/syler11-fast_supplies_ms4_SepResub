# Generated by Django 3.2 on 2022-09-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('returns', '0002_alter_returns_return_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returns',
            name='order_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]