# Generated by Django 4.1.3 on 2022-11-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_task_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.TextField(blank=True, default='-', max_length=3000, null=True, verbose_name='Opisanie'),
        ),
    ]