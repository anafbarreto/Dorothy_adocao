# Generated by Django 4.2.11 on 2024-04-11 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_adocao', '0002_adotante_animal_adotado'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Adocao',
        ),
    ]