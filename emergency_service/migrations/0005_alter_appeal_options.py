# Generated by Django 4.1.1 on 2022-11-07 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emergency_service', '0004_alter_appeal_options_alter_appeal_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appeal',
            options={'ordering': ['-date'], 'verbose_name': 'Обращение', 'verbose_name_plural': 'Обращения'},
        ),
    ]