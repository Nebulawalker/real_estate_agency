# Generated by Django 2.2.24 on 2023-04-11 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20230410_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='property.Flat', verbose_name='Квартира'),
        ),
    ]
