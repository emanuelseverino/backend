# Generated by Django 3.2.7 on 2021-09-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20210914_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='profissional',
            field=models.BooleanField(default=False, verbose_name='Profissional'),
        ),
    ]