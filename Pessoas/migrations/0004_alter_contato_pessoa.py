# Generated by Django 4.1.2 on 2022-11-10 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0003_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contatos', to='Pessoas.pessoa'),
        ),
    ]
