# Generated by Django 5.0.6 on 2024-07-17 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplebackend', '0003_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
