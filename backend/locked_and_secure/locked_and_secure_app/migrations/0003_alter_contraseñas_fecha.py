# Generated by Django 4.1.2 on 2023-05-21 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locked_and_secure_app', '0002_usuarios_clave_alter_contraseñas_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contraseñas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 5, 21, 8, 58, 7, 325385, tzinfo=datetime.timezone.utc)),
        ),
    ]
