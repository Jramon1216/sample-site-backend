# Generated by Django 5.0.6 on 2024-07-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplebackend', '0002_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
