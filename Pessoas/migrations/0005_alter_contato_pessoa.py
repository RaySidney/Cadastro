# Generated by Django 4.1.2 on 2022-11-10 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0004_alter_contato_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pessoas.pessoa'),
        ),
    ]