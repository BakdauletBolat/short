# Generated by Django 4.1 on 2022-08-05 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_url_creation_date_alter_url_original_url_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='main.url'),
        ),
    ]
