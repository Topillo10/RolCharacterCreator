# Generated by Django 4.0.5 on 2023-05-01 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreacionPJ', '0014_personaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='razasidiomas',
            name='grados',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='razasidiomas',
            name='idiomas',
            field=models.CharField(max_length=30),
        ),
    ]
