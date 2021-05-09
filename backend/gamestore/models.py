from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Genre(models.Model):
    genreid = models.AutoField(db_column='genreID', primary_key=True)  # Field name made lowercase.
    genre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.genre

    class Meta:
        managed = False
        db_table = 'genre'


class Game(models.Model):
    gameid = models.AutoField(db_column='gameID', primary_key=True)  # Field name made lowercase.
    gamename = models.CharField(db_column='gameName', max_length=50)  # Field name made lowercase.
    datereleased = models.DateField(db_column='dateReleased', blank=True, null=True)  # Field name made lowercase.
    gamedescription = models.CharField(db_column='gameDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    genres = models.ManyToManyField(Genre, through="Gamegenre")

    def __str__(self):
        return self.gamename

    class Meta:
        managed = False
        db_table = 'game'


class Gamegenre(models.Model):
    genreid = models.ForeignKey(Genre, on_delete=models.CASCADE, db_column='genreID') # Field name made lowercase.
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, db_column='gameID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gamegenre'
        unique_together = (('genreid', 'gameid'),)


class Playstore(models.Model):
    playstorerow = models.AutoField(db_column='playStoreRow', primary_key=True)  # Field name made lowercase.
    game = models.ForeignKey(Game, on_delete=models.CASCADE, db_column='game', null=True)  # Field name made lowercase.
    gameprice = models.DecimalField(db_column='gamePrice', max_digits=18, decimal_places=2)  # Field name made lowercase.
    discount = models.FloatField(blank=True, null=True)
    dateadded = models.DateField(db_column='dateAdded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playstore'


class Playstorehistory(models.Model):
    playstorerow = models.AutoField(db_column='playStoreRow', primary_key=True)  # Field name made lowercase.
    gameid = models.IntegerField(db_column='gameID')  # Field name made lowercase.
    gameprice = models.DecimalField(db_column='gamePrice', max_digits=18, decimal_places=2)  # Field name made lowercase.
    discount = models.FloatField(blank=True, null=True)
    dateadded = models.DateField(db_column='dateAdded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playstorehistory'
