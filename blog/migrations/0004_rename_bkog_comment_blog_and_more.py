# Generated by Django 5.0.4 on 2024-04-12 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='bkog',
            new_name='blog',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='create_ate',
            new_name='created_at',
        ),
    ]
