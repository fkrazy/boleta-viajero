# Generated by Django 3.1.7 on 2021-04-28 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empresa_transporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='transporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='', max_length=15)),
                ('nombre', models.CharField(default='', max_length=15)),
                ('numero', models.IntegerField()),
                ('matricula', models.CharField(default='', max_length=10)),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transporte.empresa_transporte')),
            ],
        ),
    ]