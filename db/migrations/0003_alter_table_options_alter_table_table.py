# Generated by Django 4.2.10 on 2024-02-20 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_table_options_alter_table_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'verbose_name': 'Таблица', 'verbose_name_plural': 'Таблицы'},
        ),
        migrations.AlterModelTable(
            name='table',
            table=None,
        ),
    ]
