# Generated by Django 4.0.3 on 2022-05-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_fertilizer_fert_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FertService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertname', models.CharField(max_length=100)),
                ('fertilize_date', models.DateField(blank=True, null=True)),
                ('frequency', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['-fertilize_date'],
            },
        ),
        migrations.RemoveField(
            model_name='fertilizer',
            name='fertilize_date',
        ),
        migrations.RemoveField(
            model_name='fertilizer',
            name='frequency',
        ),
    ]