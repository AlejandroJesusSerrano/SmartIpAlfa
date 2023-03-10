# Generated by Django 4.1.7 on 2023-03-06 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20, verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'db_table': 'MarcaDispositivo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DevType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_type', models.CharField(max_length=20, verbose_name='Tipos de Dispositivo')),
            ],
            options={
                'verbose_name': 'Tipo de Dispositivo',
                'verbose_name_plural': 'Tipos de Dispositivos',
                'db_table': 'TipoDispositivo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20, verbose_name='Modelo')),
                ('img', models.ImageField(upload_to='DevImages/%Y/%m/%d')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models_brand', to='devmanager.brand')),
                ('dev_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models_dev_type', to='devmanager.brand')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
                'db_table': 'ModeloDispositivo',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='brand',
            name='dev_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands_model', to='devmanager.devtype'),
        ),
    ]
