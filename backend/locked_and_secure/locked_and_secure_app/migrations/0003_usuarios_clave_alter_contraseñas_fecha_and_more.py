# Generated by Django 4.1.7 on 2023-05-31 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locked_and_secure_app', '0002_grupos_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='clave',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contraseñas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 5, 31, 9, 56, 25, 31296, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='grupos',
            name='imagen',
            field=models.TextField(default=None, null=True),
        ),
    ]
