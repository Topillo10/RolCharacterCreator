# Generated by Django 4.0.5 on 2023-05-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreacionPJ', '0013_habilidades_secundarias_razasidiomas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuerza', models.IntegerField()),
                ('agilidad', models.IntegerField()),
                ('constitucion', models.IntegerField()),
                ('inteligencia', models.IntegerField()),
                ('intuicion', models.IntegerField()),
                ('presencia', models.IntegerField()),
                ('apariencia', models.IntegerField()),
                ('nombre_pj', models.CharField(blank=True, max_length=30, null=True)),
                ('usuario', models.CharField(blank=True, max_length=255, null=True)),
                ('raza', models.CharField(blank=True, max_length=30, null=True)),
                ('estatura', models.FloatField(blank=True, null=True)),
                ('peso', models.IntegerField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, max_length=1, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('pelo', models.CharField(blank=True, max_length=50, null=True)),
                ('ojos', models.CharField(blank=True, max_length=50, null=True)),
                ('especial_fisico', models.CharField(blank=True, max_length=100, null=True)),
                ('personalidad', models.CharField(blank=True, max_length=50, null=True)),
                ('motivacion', models.CharField(blank=True, max_length=100, null=True)),
                ('alineamiento', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('familia', models.CharField(blank=True, max_length=50, null=True)),
                ('profesion', models.CharField(blank=True, max_length=30, null=True)),
                ('nivel', models.IntegerField(blank=True, null=True)),
                ('dominio_magico', models.CharField(blank=True, max_length=30, null=True)),
                ('experiencia', models.IntegerField(blank=True, null=True)),
                ('gr_sin_armadura', models.IntegerField(blank=True, null=True)),
                ('gr_cuero', models.IntegerField(blank=True, null=True)),
                ('gr_cuero_endurecido', models.IntegerField(blank=True, null=True)),
                ('gr_cota_de_malla', models.IntegerField(blank=True, null=True)),
                ('gr_coraza', models.IntegerField(blank=True, null=True)),
                ('gr_de_filo', models.IntegerField(blank=True, null=True)),
                ('gr_contundentes', models.IntegerField(blank=True, null=True)),
                ('gr_a_dos_manos', models.IntegerField(blank=True, null=True)),
                ('gr_arrojadizas', models.IntegerField(blank=True, null=True)),
                ('gr_proyectiles', models.IntegerField(blank=True, null=True)),
                ('gr_armas_de_asta', models.IntegerField(blank=True, null=True)),
                ('gr_escudo', models.IntegerField(blank=True, null=True)),
                ('gr_trepar', models.IntegerField(blank=True, null=True)),
                ('gr_montar', models.IntegerField(blank=True, null=True)),
                ('gr_nadar', models.IntegerField(blank=True, null=True)),
                ('gr_rastrear', models.IntegerField(blank=True, null=True)),
                ('gr_emboscar', models.IntegerField(blank=True, null=True)),
                ('gr_acechar_y_esconderse', models.IntegerField(blank=True, null=True)),
                ('gr_abrir_cerraduras', models.IntegerField(blank=True, null=True)),
                ('gr_desactivar_trampas', models.IntegerField(blank=True, null=True)),
                ('gr_leer_runas', models.IntegerField(blank=True, null=True)),
                ('gr_usar_objetos', models.IntegerField(blank=True, null=True)),
                ('gr_sortilegios_dirigidos', models.IntegerField(blank=True, null=True)),
                ('gr_percepcion', models.IntegerField(blank=True, null=True)),
                ('gr_liderazgo_e_influencia', models.IntegerField(blank=True, null=True)),
                ('gr_desarrollo_fisico', models.CharField(blank=True, max_length=255, null=True)),
                ('gr_puntos_de_poder', models.CharField(blank=True, max_length=255, null=True)),
                ('esp_sin_armadura', models.IntegerField(blank=True, null=True)),
                ('esp_cuero', models.IntegerField(blank=True, null=True)),
                ('esp_cuero_endurecido', models.IntegerField(blank=True, null=True)),
                ('esp_cota_de_malla', models.IntegerField(blank=True, null=True)),
                ('esp_coraza', models.IntegerField(blank=True, null=True)),
                ('esp_de_filo', models.IntegerField(blank=True, null=True)),
                ('esp_contundentes', models.IntegerField(blank=True, null=True)),
                ('esp_a_dos_manos', models.IntegerField(blank=True, null=True)),
                ('esp_arrojadizas', models.IntegerField(blank=True, null=True)),
                ('esp_proyectiles', models.IntegerField(blank=True, null=True)),
                ('esp_armas_de_asta', models.IntegerField(blank=True, null=True)),
                ('esp_escudo', models.IntegerField(blank=True, null=True)),
                ('esp_trepar', models.IntegerField(blank=True, null=True)),
                ('esp_montar', models.IntegerField(blank=True, null=True)),
                ('esp_nadar', models.IntegerField(blank=True, null=True)),
                ('esp_rastrear', models.IntegerField(blank=True, null=True)),
                ('esp_emboscar', models.IntegerField(blank=True, null=True)),
                ('esp_acechar_y_esconderse', models.IntegerField(blank=True, null=True)),
                ('esp_abrir_cerraduras', models.IntegerField(blank=True, null=True)),
                ('esp_desactivar_trampas', models.IntegerField(blank=True, null=True)),
                ('esp_leer_runas', models.IntegerField(blank=True, null=True)),
                ('esp_usar_objetos', models.IntegerField(blank=True, null=True)),
                ('esp_sortilegios_dirigidos', models.IntegerField(blank=True, null=True)),
                ('esp_percepcion', models.IntegerField(blank=True, null=True)),
                ('esp_liderazgo_e_influencia', models.IntegerField(blank=True, null=True)),
                ('esp_desarrollo_fisico', models.IntegerField(blank=True, null=True)),
                ('esp_puntos_de_poder', models.IntegerField(blank=True, null=True)),
                ('esp_esencia', models.IntegerField(blank=True, null=True)),
                ('esp_canalizacion', models.IntegerField(blank=True, null=True)),
                ('esp_veneno', models.IntegerField(blank=True, null=True)),
                ('esp_enfermedad', models.IntegerField(blank=True, null=True)),
                ('esp_frio', models.IntegerField(blank=True, null=True)),
                ('esp_calor', models.IntegerField(blank=True, null=True)),
                ('obj_sin_armadura', models.IntegerField(blank=True, null=True)),
                ('obj_cuero', models.IntegerField(blank=True, null=True)),
                ('obj_cuero_endurecido', models.IntegerField(blank=True, null=True)),
                ('obj_cota_de_malla', models.IntegerField(blank=True, null=True)),
                ('obj_coraza', models.IntegerField(blank=True, null=True)),
                ('obj_de_filo', models.IntegerField(blank=True, null=True)),
                ('obj_contundentes', models.IntegerField(blank=True, null=True)),
                ('obj_a_dos_manos', models.IntegerField(blank=True, null=True)),
                ('obj_arrojadizas', models.IntegerField(blank=True, null=True)),
                ('obj_proyectiles', models.IntegerField(blank=True, null=True)),
                ('obj_armas_de_asta', models.IntegerField(blank=True, null=True)),
                ('obj_escudo', models.IntegerField(blank=True, null=True)),
                ('obj_trepar', models.IntegerField(blank=True, null=True)),
                ('obj_montar', models.IntegerField(blank=True, null=True)),
                ('obj_nadar', models.IntegerField(blank=True, null=True)),
                ('obj_rastrear', models.IntegerField(blank=True, null=True)),
                ('obj_emboscar', models.IntegerField(blank=True, null=True)),
                ('obj_acechar_y_esconderse', models.IntegerField(blank=True, null=True)),
                ('obj_abrir_cerraduras', models.IntegerField(blank=True, null=True)),
                ('obj_desactivar_trampas', models.IntegerField(blank=True, null=True)),
                ('obj_leer_runas', models.IntegerField(blank=True, null=True)),
                ('obj_usar_objetos', models.IntegerField(blank=True, null=True)),
                ('obj_sortilegios_dirigidos', models.IntegerField(blank=True, null=True)),
                ('obj_percepcion', models.IntegerField(blank=True, null=True)),
                ('obj_liderazgo_e_influencia', models.IntegerField(blank=True, null=True)),
                ('obj_desarrollo_fisico', models.IntegerField(blank=True, null=True)),
                ('obj_puntos_de_poder', models.IntegerField(blank=True, null=True)),
                ('obj_esencia', models.IntegerField(blank=True, null=True)),
                ('obj_canalizacion', models.IntegerField(blank=True, null=True)),
                ('obj_veneno', models.IntegerField(blank=True, null=True)),
                ('obj_enfermedad', models.IntegerField(blank=True, null=True)),
                ('obj_frio', models.IntegerField(blank=True, null=True)),
                ('obj_calor', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
