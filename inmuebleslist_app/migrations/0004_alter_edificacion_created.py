# Generated by Django 3.2.8 on 2022-10-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebleslist_app', '0003_edificacion_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificacion',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]