# Generated by Django 4.2 on 2023-04-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_menu_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='item_name',
            field=models.CharField(max_length=50),
        ),
    ]
