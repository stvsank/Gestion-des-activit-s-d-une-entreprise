# Generated by Django 4.1.3 on 2022-11-24 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_depannage_caractéristique_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antenne',
            name='client',
        ),
        migrations.RemoveField(
            model_name='routeur',
            name='client',
        ),
        migrations.AddField(
            model_name='client',
            name='antenne',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.antenne'),
        ),
        migrations.AddField(
            model_name='client',
            name='routeur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.routeur'),
        ),
    ]