# Generated by Django 4.0.3 on 2022-05-25 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_date_fertilizer_fert_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizer',
            name='fert_date',
            field=models.DateField(verbose_name='Fertilize Date'),
        ),
    ]