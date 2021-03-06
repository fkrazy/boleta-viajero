# Generated by Django 3.1.7 on 2021-04-29 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0002_auto_20210427_2051'),
        ('viajeros', '0001_creacion_viajeros'),
        ('paises', '0003_create_aduanas'),
        ('bitacora', '0001_bitacora'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitacora',
            name='aduana',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='paises.aduana'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='direccion',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='pais_destino',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='paises_destino', to='paises.pais', verbose_name='pais'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='transporte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transporte.transporte'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='viajero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='viajeros.viajero'),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='pais_procedencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='paises_bitacora', to='paises.pais', verbose_name='pais'),
        ),
    ]
