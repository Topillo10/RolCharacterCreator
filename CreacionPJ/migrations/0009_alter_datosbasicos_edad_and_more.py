# Generated by Django 4.1.7 on 2023-04-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreacionPJ', '0008_caracteristicas_delete_tiradas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosbasicos',
            name='edad',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='datosbasicos',
            name='especial_fisico',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='datosbasicos',
            name='estatura',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='datosbasicos',
            name='motivacion',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='datosbasicos',
            name='nombre_pj',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='datosbasicos',
            name='ojos',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='datosbasicos',
            name='pelo',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='datosbasicos',
            name='personalidad',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='datosbasicos',
            name='peso',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='datosbasicos',
            name='status',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
