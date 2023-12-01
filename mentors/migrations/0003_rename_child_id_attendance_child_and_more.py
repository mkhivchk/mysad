# Generated by Django 4.2.7 on 2023-11-27 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0002_alter_mentor_password_alter_mentor_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='child_id',
            new_name='child',
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='mentor_id',
            new_name='mentor',
        ),
        migrations.AddField(
            model_name='attendance',
            name='child_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]