# Generated by Django 2.1.4 on 2018-12-15 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='projects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
