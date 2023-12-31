# Generated by Django 4.2.7 on 2023-12-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='value',
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('WORKING', 'Working'), (
                'DONE', 'Done'), ('OVERDUE', 'Overdue')], default='OPEN', max_length=10),
        ),
    ]
