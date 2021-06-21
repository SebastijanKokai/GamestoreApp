# import sys
# import os
# import pathlib
# target_path = pathlib.Path(os.path.abspath(__file__)).parents[3]
# sys.path.append(target_path)
from django.db import models
from django.contrib.auth.models import AbstractUser
from gamestore.models import Game

class AuthUser(AbstractUser):
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    user_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'authuser'

class Friendlist(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, db_column='userID', related_name='users')  # Field name made lowercase.
    friend = models.ForeignKey(AuthUser, on_delete=models.CASCADE, db_column='friendID', related_name='friends') # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'friendlist'
        unique_together = (('user', 'friend'),)


class Wishlist(models.Model):
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, db_column='gameID')  # Field name made lowercase.
    userid = models.ForeignKey(AuthUser, on_delete=models.CASCADE, db_column='userID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'wishlist'
        unique_together = (('gameid', 'userid'),)

class Gamelibrary(models.Model):
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, db_column='gameID')  # Field name made lowercase.
    userid = models.ForeignKey(AuthUser, on_delete=models.CASCADE, db_column='userID')  # Field name made lowercase.
    totaltimeplayed = models.IntegerField(db_column='totalTimePlayed', blank=True, null=True)  # Field name made lowercase.
    lasttimeplayed = models.DateField(db_column='lastTimePlayed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'gamelibrary'
        unique_together = (('gameid', 'userid'),)

