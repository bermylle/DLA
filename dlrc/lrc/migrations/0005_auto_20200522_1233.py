# Generated by Django 3.0.6 on 2020-05-22 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lrc', '0004_tutor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='role',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
    ]
