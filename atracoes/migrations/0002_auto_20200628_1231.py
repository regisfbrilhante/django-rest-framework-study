# Generated by Django 2.2 on 2020-06-28 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_pontoturistico_avaliacoes'),
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Atracao',
            new_name='Atracoes',
        ),
    ]