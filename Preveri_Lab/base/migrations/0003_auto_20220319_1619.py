# Generated by Django 3.2.9 on 2022-03-19 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_tittle_task_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['completed']},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='completed',
        ),
    ]