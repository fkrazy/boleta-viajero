# Generated by Django 3.1.7 on 2021-04-28 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paises', '0002_creacion_paises'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aduana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=80)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='paises', to='paises.pais', verbose_name='pais')),
            ],
        ),
    ]
