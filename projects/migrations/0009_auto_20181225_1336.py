# Generated by Django 2.1.4 on 2018-12-25 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20181225_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.PLanguage'),
        ),
    ]
