# Generated by Django 5.0.3 on 2024-03-22 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Garagem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Modelo', to='Garagem.categoria')),
                ('marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Modelo', to='Garagem.marca')),
            ],
        ),
    ]
