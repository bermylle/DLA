# Generated by Django 3.0.6 on 2020-05-22 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_student_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='profile_pic',
            field=models.ImageField(blank=True, default='prof-icon-default.png', null=True, upload_to='profile_pics'),
        ),
    ]