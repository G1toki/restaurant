# Generated by Django 4.2.1 on 2023-05-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_casestudy'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudy',
            name='keywords',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='casestudy',
            name='processed',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]