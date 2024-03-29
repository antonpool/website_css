# Generated by Django 4.2.10 on 2024-02-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'verbose_name': 'table', 'verbose_name_plural': 'Таблицы'},
        ),
        migrations.AlterField(
            model_name='table',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='table',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(max_length=200, verbose_name='название темы'),
        ),
        migrations.AlterField(
            model_name='table',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='ссылка для статьи'),
        ),
        migrations.AlterField(
            model_name='table',
            name='text_all',
            field=models.TextField(blank=True, null=True, verbose_name='содержимое статьи'),
        ),
        migrations.AlterField(
            model_name='table',
            name='text_code',
            field=models.TextField(blank=True, null=True, verbose_name='как выглядт код'),
        ),
        migrations.AlterField(
            model_name='table',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='основная мысль'),
        ),
        migrations.AlterModelTable(
            name='table',
            table='table',
        ),
    ]
