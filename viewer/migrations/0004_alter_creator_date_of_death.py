# Generated by Django 4.2.15 on 2024-09-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_creator_created_creator_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='date_of_death',
            field=models.DateField(blank=True, null=True),
        ),
    ]
