from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Count, F, Value


from games.models import Athletes, BroadcastVideo, GamesCategory, Hitcount, Schedule, Scoreboards, HighlightsVideo

def games_dashboard(request):
    template_name = 'games/dashboard.html'

    games = GamesCategory.objects.all()
    
    return render(request, template_name, {'games': games})

def athletes_view(request):
    template_name = 'games/athletes_user.html'

    athletes = Athletes.objects.all()
    
    return render(request, template_name, {'athletes': athletes})


def gamedetails_view(request, id):

    template_name = 'games/games_details.html'

    game_details = GamesCategory.objects.get(id=id)
    scoreboard = Scoreboards.objects.filter(game=id)
    broadcast = BroadcastVideo.objects.filter(of_game=id)
    schedule = Schedule.objects.filter(for_game=id)

    return render(request, template_name, {'gdetails': game_details, 'id': id, 'scoreboard': scoreboard, 'broadcast': broadcast, 'schedule': schedule})

@login_required
def broadcast_details(request, id):

    template_name = 'games/broadcast_details.html'

    game_details = GamesCategory.objects.get(id=id)
    broadcast = BroadcastVideo.objects.filter(of_game=id)

    return render(request, template_name, {'gdetails': game_details, 'broadcast': broadcast})


def highlights_details(request, id):

    template_name = 'games/highlights_details.html'

    game_details = GamesCategory.objects.get(id=id)
    highlights = HighlightsVideo.objects.filter(game=id)

    return render(request, template_name, {'gdetails': game_details, 'highlights': highlights})

@login_required
def highlights_one(request, id):

    template_name = 'games/highlights_one.html'

    highlights = HighlightsVideo.objects.get(id=id)

    return render(request, template_name, {'highlights': highlights})

@login_required
def broadcast_one(request, id):

    template_name = 'games/broadcast_one.html'

    broadcast = BroadcastVideo.objects.get(id=id)
    if Hitcount.objects.filter(broadcast_name=str(broadcast)):
        Hitcount.objects.filter(broadcast_name=str(broadcast)).update(hit_count = F('hit_count')+1)
    else:
        Hitcount.objects.update_or_create(hit_count=1, broadcast=broadcast.video_url, broadcast_name=broadcast.broadcast_title)

    return render(request, template_name, {'broadcast': broadcast})

def scoreboard_details(request, id):

    template_name = 'games/scoreboard_details.html'

    game_details = GamesCategory.objects.get(id=id)
    scoreboard = Scoreboards.objects.filter(game=id)

    return render(request, template_name, {'gdetails': game_details, 'scoreboard': scoreboard })



def schedule_details(request, id):

    template_name = 'games/schedule_details.html'

    game_details = GamesCategory.objects.get(id=id)
    schedule = Schedule.objects.filter(for_game=id)

    return render(request, template_name, {'gdetails': game_details, 'schedule': schedule})


def logout_view(request):
    logout(request)
    return redirect('/')