# Generated by Django 3.2 on 2021-06-21 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0002_auto_20210621_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='gameid',
            new_name='game',
        ),
        migrations.AlterUniqueTogether(
            name='wishlist',
            unique_together={('game', 'userid')},
        ),
    ]