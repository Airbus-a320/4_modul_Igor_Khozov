# Generated by Django 4.2.3 on 2023-08-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0002_alter_advertisement_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='auction',
            field=models.BooleanField(help_text='Отьметьте, если торг уместен', verbose_name='Торг'),
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]