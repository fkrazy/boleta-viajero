# Generated by Django 3.1.7 on 2021-05-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajeros', '0003_tercero_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viajero',
            name='numero_documento',
            field=models.CharField(default='', max_length=45),
        ),
    ]