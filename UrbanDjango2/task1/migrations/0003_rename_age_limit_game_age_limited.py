# Generated by Django 5.0.7 on 2024-07-14 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_remove_game_buyer_game_buyer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='age_limit',
            new_name='age_limited',
        ),
    ]
