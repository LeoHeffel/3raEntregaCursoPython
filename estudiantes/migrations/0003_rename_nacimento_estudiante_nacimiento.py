# Generated by Django 4.2.5 on 2023-09-23 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0002_remove_estudiante_email_estudiante_nacimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='nacimento',
            new_name='nacimiento',
        ),
    ]