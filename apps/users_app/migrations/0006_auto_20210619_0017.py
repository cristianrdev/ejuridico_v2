# Generated by Django 3.1.7 on 2021-06-19 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0005_auto_20210619_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawsuit_state',
            name='name_state',
            field=models.CharField(default='escritura creada', max_length=45),
        ),
    ]
