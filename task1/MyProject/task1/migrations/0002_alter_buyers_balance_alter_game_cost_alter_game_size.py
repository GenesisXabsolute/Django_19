# Generated by Django 5.1.3 on 2024-11-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyers',
            name='balance',
            field=models.DecimalField(decimal_places=6, max_digits=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='cost',
            field=models.DecimalField(decimal_places=6, max_digits=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='size',
            field=models.DecimalField(decimal_places=6, max_digits=100),
        ),
    ]