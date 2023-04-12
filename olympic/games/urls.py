from django.urls import path

from . import views
# links of the pages which we have made in application
urlpatterns = [
    path('', views.games_dashboard, name='games_dashboard'),
    path('logout/', views.logout_view, name='logout_view'),
    path('game_details/<int:id>', views.gamedetails_view, name='game_details'),
    path('atheltes/', views.athletes_view, name='athletes_view'),
    path('broadcast_details/<int:id>', views.broadcast_details, name='broadcast_details'),
    path('broadcast_one/<int:id>', views.broadcast_one, name='broadcast_one'),
    path('highlights_details/<int:id>', views.highlights_details, name='highlights_details'),
    path('highlights_one/<int:id>', views.highlights_one, name='highlights_one'),
    path('scoreboard_details/<int:id>', views.scoreboard_details, name='scoreboard_details'),
    path('schedule_details/<int:id>', views.schedule_details, name='schedule_details'),

]