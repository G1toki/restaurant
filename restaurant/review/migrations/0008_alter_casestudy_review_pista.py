# Generated by Django 4.2.1 on 2023-05-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_casestudy_keywords_casestudy_processed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudy',
            name='review_pista',
            field=models.CharField(max_length=500),
        ),
    ]
