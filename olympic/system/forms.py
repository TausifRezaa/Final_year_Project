from dataclasses import field, fields
from pyexpat import model
from django import forms
from users.models import  User
from games.models import BroadcastVideo, GamesCategory, HighlightsVideo, Schedule, Scoreboards, Athletes

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

''' Games '''
class GamesUpdateForm(forms.ModelForm):
    class Meta:
        model  = GamesCategory
        fields = '__all__'

class AddGamesForm(forms.ModelForm):
    class Meta:
        model= GamesCategory
        fields = '__all__'


''' Highlights '''
class AddHighlightsForm(forms.ModelForm):
    class Meta:
        model= HighlightsVideo
        fields = '__all__'

class HighlightsUpdateForm(forms.ModelForm):
    class Meta:
        model  = HighlightsVideo
        fields = '__all__'


''' Broadcasts '''
class AddBroadcastsForm(forms.ModelForm):
    class Meta:
        model= BroadcastVideo
        fields = '__all__'

class BroadcastsUpdateForm(forms.ModelForm):
    class Meta:
        model  = BroadcastVideo
        fields = '__all__'

''' Schedule '''
class AddScheduleForm(forms.ModelForm):
    class Meta:
        model= Schedule
        fields = '__all__'

class ScheduleUpdateForm(forms.ModelForm):
    class Meta:
        model  = Schedule
        fields = '__all__'

''' Scoreboard '''
class AddScoreboardForm(forms.ModelForm):
    class Meta:
        model= Scoreboards
        fields = '__all__'
    
class ScoreboardUpdateForm(forms.ModelForm):
    class Meta:
        model  = Scoreboards
        fields = '__all__'

''' Athletes '''
class AddAthletesForm(forms.ModelForm):
    class Meta:
        model= Athletes
        fields = '__all__'
    
class AthletesUpdateForm(forms.ModelForm):
    class Meta:
        model  = Athletes
        fields = '__all__'