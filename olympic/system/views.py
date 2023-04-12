from email.policy import HTTP
from django.shortcuts import render, redirect
from users.models import User
from games.models import Athletes, GamesCategory, BroadcastVideo, HighlightsVideo, Hitcount, Schedule, Scoreboards
from django.contrib.auth.forms import PasswordChangeForm

from .forms import AddAthletesForm, AthletesUpdateForm, GamesUpdateForm, UserUpdateForm, AddGamesForm, AddHighlightsForm, HighlightsUpdateForm, AddBroadcastsForm, BroadcastsUpdateForm, AddScheduleForm, ScheduleUpdateForm, AddScoreboardForm, ScoreboardUpdateForm
from django.http import HttpResponse

import csv


def admin_dashboard(request):
    template_name = 'system/adashboard.html'
    current_user = request.user
    if current_user:
        ausers = User.objects.all()
        ucount = User.objects.all().count()
        gamescount = GamesCategory.objects.all().count()
        broadcastscount = BroadcastVideo.objects.all().count()
        return render(request, template_name, {'ausers': ausers, 'ucount': ucount, 'gamescount': gamescount, 'broadcastscount': broadcastscount})
    else:
        return render(request, 'games/dashboard.html')


def admin_users(request, id):
    template_name = 'system/user_details.html'

    if request.method=="POST":
        auser = User.objects.get(id = id)
        user_form = UserUpdateForm(request.POST, instance=auser)
        # conuser_form = ConUserUpdateForm(request.POST, instance=conuser)
        # passwordchange_form = PasswordChangeForm(request.POST, auser)
        if user_form.is_valid():
            user_form.save()
            return redirect('/system/')
        else:
            return redirect('/')
    else:
        auser = User.objects.get(id = id)
        user_form = UserUpdateForm(instance=auser)
        # user_form = UserUpdateForm(instance = conuser)
        # passwordchange_form = PasswordChangeForm(auser)

    context = {
        'user_form': user_form,
        # 'conuser_form': conuser_form,
        # 'passwordchange_form': passwordchange_form,
    }

    return render(request, template_name, {'user_form': user_form, 'auser': auser})


# """"""Games""""""

def admin_games(request):
    template_name = 'system/agames.html'
    games = GamesCategory.objects.all()

    ucount = User.objects.all().count()
    gamescount = GamesCategory.objects.all().count()
    broadcastscount = BroadcastVideo.objects.all().count()

    return render(request, template_name, {'games': games, 'ucount': ucount, 'gamescount': gamescount, 'broadcastscount': broadcastscount})

def export_to_csv(request):
    games = GamesCategory.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=games.csv'
    writer = csv.writer(response)
    writer.writerow(['Game Name', 'Game Description', 'Gamme Image'])
    game_fields = games.values_list('game_name','game_description','game_image')
    for game in game_fields:
        writer.writerow(game)
    return response

def admin_add_games(request):
    template_name = 'system/add_games.html'
    if request.method=="POST":
        # game = GamesCategory.objects.get(id = id)
        game_form = AddGamesForm(request.POST or None, request.FILES or None)
        if game_form.is_valid():
            game_form.save()
            return redirect('/system/agames/')
    else:
        # game = GamesCategory.objects.get(id = id)
        game_form = AddGamesForm()
    return render(request, template_name, {'game_form': game_form})

def admin_games_details(request, id):
    template_name = "system/game_details.html"
    if request.method=="POST":
        game = GamesCategory.objects.get(id = id)
        game_form = GamesUpdateForm(request.POST, request.FILES or None, instance=game)
        if game_form.is_valid():
            game_form.save()
            return redirect('/system/agames/')
        else:
            return redirect('/')
    else:
        game = GamesCategory.objects.get(id = id)
        game_form = GamesUpdateForm(instance=game)
        
    return render(request, template_name, {'game_form': game_form})

def delete_game(request, id):
    to_delete = GamesCategory.objects.get(id=id)
    to_delete.delete()
    return redirect('/system/agames/')


# Highlights

def admin_highlights(request):
    template_name = 'system/ahighlights.html'
    highlights = HighlightsVideo.objects.all()

    ucount = User.objects.all().count()
    gamescount = GamesCategory.objects.all().count()
    broadcastscount = BroadcastVideo.objects.all().count()

    return render(request, template_name, {'highlights': highlights, 'ucount': ucount, 'gamescount': gamescount, 'broadcastscount': broadcastscount})

def admin_add_highlights(request):
    template_name = 'system/add_highlights.html'
    if request.method=="POST":
        game_form = AddHighlightsForm(request.POST or None, request.FILES or None)
        if game_form.is_valid():
            game_form.save()
            return redirect('/system/ahighlights/')
    else:
        # game = GamesCategory.objects.get(id = id)
        game_form = AddHighlightsForm()
    return render(request, template_name, {'game_form': game_form})

def admin_highlights_details(request, id):
    template_name = "system/highlights_details.html"
    if request.method=="POST":
        game = HighlightsVideo.objects.get(id = id)
        game_form = HighlightsUpdateForm(request.POST, request.FILES or None, instance=game)
        if game_form.is_valid():
            game_form.save()
            return redirect('/system/ahighlights/')
        else:
            return redirect('/')
    else:
        game = HighlightsVideo.objects.get(id = id)
        game_form = HighlightsUpdateForm(instance=game)
        
    return render(request, template_name, {'game_form': game_form})

def delete_highights(request, id):
    to_delete = HighlightsVideo.objects.get(id=id)
    to_delete.delete()
    return redirect('/system/ahighlights/')



''' Broadcasts '''
def admin_broadcasts(request):
    template_name = 'system/abroadcasts.html'
    broadcasts = BroadcastVideo.objects.all()

    ucount = User.objects.all().count()
    gamescount = GamesCategory.objects.all().count()
    broadcastscount = BroadcastVideo.objects.all().count()

    return render(request, template_name, {'broadcasts': broadcasts, 'ucount': ucount, 'gamescount': gamescount, 'broadcastscount': broadcastscount})

def admin_add_broadcasts(request):
    template_name = 'system/add_broadcasts.html'
    if request.method=="POST":
        game_form = AddBroadcastsForm(request.POST or None, request.FILES or None)
        if game_form.is_valid():
            game_form.save()
            return redirect('/system/abroadcasts/')
    else:
        # game = GamesCategory.objects.get(id = id)
        game_form = AddBroadcastsForm()
    return render(request, template_name, {'game_form': game_form})

def admin_broadcasts_details(request, id):
    template_name = "system/broadcasts_details.html"
    if request.method=="POST":
        game = BroadcastVideo.objects.get(id = id)
        game_form = BroadcastsUpdateForm(request.POST, request.FILES or None, instance=game)
        if game_form.is_valid():
            game_form.save()
            return redirect('/system/abroadcasts/')
        else:
            return redirect('/')
    else:
        game = BroadcastVideo.objects.get(id = id)
        game_form = BroadcastsUpdateForm(instance=game)
        
    return render(request, template_name, {'game_form': game_form})

def delete_broadcasts(request, id):
    to_delete = BroadcastVideo.objects.get(id=id)
    to_delete.delete()
    return redirect('/system/abroadcasts/')


'''Schedule'''
def admin_schedule(request):
    template_name = 'system/aschedule.html'
    schedule = Schedule.objects.all()

    ucount = User.objects.all().count()
    gamescount = GamesCategory.objects.all().count()
    broadcastscount = BroadcastVideo.objects.all().count()

    return render(request, template_name, {'schedule': schedule, 'ucount': ucount, 'gamescount': gamescount, 'broadcastscount': broadcastscount})

def export_to_csv_schedule(request):
    games = Schedule.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=schedule.csv'
    writer = csv.writer(response)
    writer.writerow(['Game Name', 'Schedule Title', 'Match Details', 'Schedule Image'])
    game_fields = games.values_list('for_game','schedule_title', 'match_details', 'schedule_img')
    for game in game_fields:
        writer.writerow(game)
    return response

def admin_add_schedule(request):
    template_name = 'system/add_schedule.html'
    if request.method=="POST":
        game_form = AddScheduleForm(request.POST or None, request.FILES or None)
        if game_form.is_valid():
            game_form.save()
            return redirect('/system/aschedule/')
    else:
        # game = GamesCategory.objects.get(id = id)
        game_form = AddScheduleForm()
    return render(request, template_name, {'game_form': game_form})

def admin_schedule_details(request, id):
    template_name = "system/schedule_details.html"
    if request.method=="POST":
        game = Schedule.objects.get(id = id)
        game_form = ScheduleUpdateForm(request.POST, request.FILES or None, instance=game)
        if game_form.is_valid():
            game_form.save()
            print("Right")
            return redirect('/system/aschedule/')
        else:
            print("wrong")
            return redirect('/')
    else:
        game = Schedule.objects.get(id = id)
        game_form = ScheduleUpdateForm(instance=game)
        
    return render(request, template_name, {'game_form': game_form})

def delete_schedule(request, id):
    to_delete = Schedule.objects.get(id=id)
    to_delete.delete()
    return redirect('/system/aschedule/')


''' Scoreboards '''
def admin_scoreboards(request):
    template_name = 'system/ascoreboards.html'
    scoreboards = Scoreboards.objects.all()

    ucount = User.objects.all().count()
    gamescount = GamesCategory.objects.all().count()
    broadcastscount = BroadcastVideo.objects.all().count()

    return render(request, template_name, {'scoreboards': scoreboards, 'ucount': ucount, 'gamescount': gamescount, 'broadcastscount': broadcastscount})

def admin_add_scoreboards(request):
    template_name = 'system/add_scoreboards.html'
    if request.method=="POST":
        game_form = AddScoreboardForm(request.POST or None, request.FILES or None)
        if game_form.is_valid():
            game_form.save()
            return redirect('/system/ascoreboards/')
    else:
        # game = GamesCategory.objects.get(id = id)
        game_form = AddScoreboardForm()
    return render(request, template_name, {'game_form': game_form})

def admin_scoreboards_details(request, id):
    template_name = "system/scoreboards_details.html"
    if request.method=="POST":
        game = Scoreboards.objects.get(id = id)
        game_form = ScoreboardUpdateForm(request.POST, request.FILES or None, instance=game)
        if game_form.is_valid():
            game_form.save()
            return redirect('/system/ascoreboards/')
        else:
            return redirect('/')
    else:
        game = Scoreboards.objects.get(id = id)
        game_form = ScoreboardUpdateForm(instance=game)
        
    return render(request, template_name, {'game_form': game_form})

def delete_scoreboards(request, id):
    to_delete = Scoreboards.objects.get(id=id)
    to_delete.delete()
    return redirect('/system/ascoreboards/')


''' Athletes '''
def admin_athletes(request):
    template_name = 'system/athletes.html'
    athletes = Athletes.objects.all()

    ucount = User.objects.all().count()
    gamescount = GamesCategory.objects.all().count()
    broadcastscount = BroadcastVideo.objects.all().count()

    return render(request, template_name, {'athletes': athletes, 'ucount': ucount, 'gamescount': gamescount, 'broadcastscount': broadcastscount})

def export_to_csv_schedule(request):
    games = Athletes.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=athelets.csv'
    writer = csv.writer(response)
    writer.writerow(['Atheletes Name', 'Game Title', 'Atheletes Image'])
    game_fields = games.values_list('for_game','schedule_title', 'match_details', 'schedule_img')
    for game in game_fields:
        writer.writerow(game)
    return response

def admin_add_athletes(request):
    template_name = 'system/add_athletes.html'
    if request.method=="POST":
        game_form = AddAthletesForm(request.POST or None, request.FILES or None)
        if game_form.is_valid():
            game_form.save()
            return redirect('/system/athletes/')
    else:
        # game = GamesCategory.objects.get(id = id)
        game_form = AddAthletesForm()
    return render(request, template_name, {'game_form': game_form})

def admin_athletes_details(request, id):
    template_name = "system/athletes_details.html"
    if request.method=="POST":
        game = Athletes.objects.get(id = id)
        game_form = AthletesUpdateForm(request.POST, request.FILES or None, instance=game)
        if game_form.is_valid():
            game_form.save()
            return redirect('/system/athletes/')
        else:
            return redirect('/')
    else:
        game = Athletes.objects.get(id = id)
        game_form = AthletesUpdateForm(instance=game)
        
    return render(request, template_name, {'game_form': game_form})

def delete_athletes(request, id):
    to_delete = Athletes.objects.get(id=id)
    to_delete.delete()
    return redirect('/system/athletes/')


''' Hit Counter '''
def admin_hit_counter(request):
    template_name = "system/ahitcounter.html"
    hits = Hitcount.objects.all()
    ucount = User.objects.all().count()
    gamescount = GamesCategory.objects.all().count()
    broadcastscount = BroadcastVideo.objects.all().count()

    return render(request, template_name, {'hits':hits, 'ucount': ucount, 'gamescount': gamescount, 'broadcastscount': broadcastscount})