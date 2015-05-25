from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Better(User):
    points = models.IntegerField(default=100)
    for_week = models.IntegerField(default=0)


class Song(models.Model):
	name = models.CharField
	youTube_link = models.URLField


class Betting(models.Model):
	user = models.ForeignKey(Better)
	date_time = models.DateTimeField(auto_now_add=True)
	is_won = models.BooleanField
	models.ManyToManyField(Song, through='ListOfBets')


class ListOfBets(models.Model):
	bet_id = models.ForeignKey(Betting)
	song = models.ForeignKey(Song)
	unique_together = ("bet_id", "song")
	data = models.CharField









