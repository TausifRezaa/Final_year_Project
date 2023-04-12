from logging import PlaceHolder
from django.db import models

class Athletes(models.Model):
    athlete_name =models.CharField(max_length=255)
    athlete_image = models.ImageField(upload_to='athlete_image', blank=True)
    athlete_game = models.CharField(max_length=255)
    athlete_description = models.TextField(max_length=120, blank=True)
    athlete_country = models.CharField(max_length=255)

    def __str__(self):
        return self.athlete_name

class Hitcount(models.Model):
    hit_count = models.CharField(max_length=100)
    broadcast = models.CharField(max_length=255)
    broadcast_name = models.CharField(max_length=255)

    def __str__(self):
        return self.broadcast_name

class GamesCategory(models.Model):
    game_name = models.CharField(max_length=255)
    game_description = models.TextField(max_length=500)
    game_image = models.ImageField(upload_to='game_image', blank=True)

    def __str__(self):
        return self.game_name

class Scoreboards(models.Model):
    game = models.ForeignKey(GamesCategory, on_delete = models.CASCADE)
    score = models.CharField(max_length=25)
    countries = models.CharField(max_length=200, help_text="E.g. Enter: NP vs JPN")
    score_description = models.TextField(max_length=500)

    def __str__(self):
        return self.score


class BroadcastVideo(models.Model):
    of_game = models.ForeignKey(GamesCategory, on_delete=models.CASCADE)
    broadcast_title = models.CharField(max_length=255)
    video_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.broadcast_title

class HighlightsVideo(models.Model):
    game = models.ForeignKey(GamesCategory, on_delete=models.CASCADE)
    highlights_title = models.CharField(max_length=255)
    hightlight_video_url = models.URLField(blank=True)
    hv = models.FileField(upload_to='highlights_video', blank=True)
    
    def __str__(self):
        return self.highlights_title

class Schedule(models.Model):
    for_game = models.ForeignKey(GamesCategory, on_delete=models.CASCADE)
    schedule_title = models.CharField(max_length=255)
    match_details = models.TextField(max_length=500)
    schedule_img = models.ImageField(upload_to='schedule_img', blank=True)

    def __str__(self):
        return self.schedule_title



