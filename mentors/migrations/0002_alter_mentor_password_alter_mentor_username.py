# Generated by Django 4.2.7 on 2023-11-27 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='password',
            field=models.CharField(default=django.db.models.deletion.SET_NULL, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='username',
            field=models.CharField(default=django.db.models.deletion.SET_NULL, max_length=20, null=True),
        ),
    ]
