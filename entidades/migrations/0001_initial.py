# Generated by Django 2.0.3 on 2018-03-23 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_id', models.CharField(choices=[('CUIT', 'CUIT'), ('CUIL', 'CUIL')], default='CUIT', max_length=10, verbose_name='CUIT o CUIL')),
                ('numero_id', models.CharField(max_length=20, verbose_name='Número de CUIT/CUIL')),
            ],
        ),
    ]
