# Generated by Django 2.1.4 on 2018-12-25 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20181225_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plang', to='projects.PLanguage'),
        ),
    ]