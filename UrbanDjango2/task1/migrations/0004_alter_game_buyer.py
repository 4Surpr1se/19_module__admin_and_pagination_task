# Generated by Django 5.0.7 on 2024-07-14 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_rename_age_limit_game_age_limited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='buyer',
            field=models.ManyToManyField(default=None, related_name='games', to='task1.buyer'),
        ),
    ]
