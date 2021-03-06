# Generated by Django 2.0.4 on 2018-05-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.RemoveField(
            model_name='posts',
            name='description',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='order',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='slug',
        ),
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
