from django.db import models
from django.contrib.auth.models import AbstractUser

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

class Genre(models.Model):
    genreid = models.AutoField(db_column='genreID', primary_key=True)  # Field name made lowercase.
    genre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.genre

    class Meta:
        managed = True
        db_table = 'genre'


class Game(models.Model):
    gameid = models.AutoField(db_column='gameID', primary_key=True)  # Field name made lowercase.
    gamename = models.CharField(db_column='gameName', max_length=50)  # Field name made lowercase.
    datereleased = models.DateField(db_column='dateReleased', blank=True, null=True)  # Field name made lowercase.
    gamedescription = models.CharField(db_column='gameDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gameImgUrl = models.CharField(db_column='gameImgUrl', max_length=500, blank=True, null=True)
    genres = models.ManyToManyField(Genre, through="Gamegenre")

    def __str__(self):
        return self.gamename

    class Meta:
        managed = True
        db_table = 'game'


class Gamegenre(models.Model):
    genreid = models.ForeignKey(Genre, on_delete=models.CASCADE, db_column='genreID') # Field name made lowercase.
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, db_column='gameID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'gamegenre'
        unique_together = (('genreid', 'gameid'),)


class Playstore(models.Model):
    playstorerow = models.AutoField(db_column='playStoreRow', primary_key=True)  # Field name made lowercase.
    game = models.ForeignKey(Game, on_delete=models.CASCADE, db_column='game', null=True)  # Field name made lowercase.
    gameprice = models.DecimalField(db_column='gamePrice', max_digits=18, decimal_places=2)  # Field name made lowercase.
    discount = models.FloatField(db_column='discount', blank=True, null=True)
    dateadded = models.DateField(db_column='dateAdded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'playstore'


class Playstorehistory(models.Model):
    playstorerow = models.AutoField(db_column='playStoreRow', primary_key=True)  # Field name made lowercase.
    gameid = models.IntegerField(db_column='gameID')  # Field name made lowercase.
    gameprice = models.DecimalField(db_column='gamePrice', max_digits=18, decimal_places=2)  # Field name made lowercase.
    discount = models.FloatField(blank=True, null=True)
    dateadded = models.DateField(db_column='dateAdded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'playstorehistory'

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

