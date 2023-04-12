from django.urls import path

from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('ausers/<uuid:id>', views.admin_users, name='admin_users'),

    path('agames/', views.admin_games, name='admin_games'),
    path('addagames/', views.admin_add_games, name='admin_add_games'),
    path('downloadgames/', views.export_to_csv, name='export_to_csv'),
    path('agames/<int:id>', views.admin_games_details, name='admin_games_details'),
    path('deleteagames/<int:id>', views.delete_game, name='delete_game'),

    path('ahighlights/', views.admin_highlights, name='admin_highlights'),
    path('addahiglights/', views.admin_add_highlights, name='admin_add_highlights'),
    path('ahighlights/<int:id>', views.admin_highlights_details, name='admin_highlights_details'),
    path('deleteahighlights/<int:id>', views.delete_highights, name='delete_highlights'),
    
    
    
    path('abroadcasts/', views.admin_broadcasts, name='admin_broadcasts'),
    path('addabroadcasts/', views.admin_add_broadcasts, name='admin_add_broadcasts'),
    path('abroadcasts/<int:id>', views.admin_broadcasts_details, name='admin_broadcasts_details'),
    path('deleteabroadcasts/<int:id>', views.delete_broadcasts, name='delete_broadcasts'),
    
    
    
    path('aschedule/', views.admin_schedule, name='admin_schedule'),
    path('addaschedule/', views.admin_add_schedule, name='admin_add_schedule'),
    path('downloadschedule/', views.export_to_csv_schedule, name='export_to_csv_schedule'),

    path('aschedule/<int:id>', views.admin_schedule_details, name='admin_schedule_details'),
    path('deleteaschedule/<int:id>', views.delete_schedule, name='delete_schedule'),
    
    
    path('ascoreboards/', views.admin_scoreboards, name='admin_scoreboards'),
    path('addascoreboards/', views.admin_add_scoreboards, name='admin_add_scoreboards'),
    path('ascoreboards/<int:id>', views.admin_scoreboards_details, name='admin_scoreboards_details'),
    path('deleteascoreboards/<int:id>', views.delete_scoreboards, name='delete_scoreboards'),
    

    path('athletes/', views.admin_athletes, name='admin_athletes'),
    path('addathletes/', views.admin_add_athletes, name='admin_add_athletes'),
    path('athletes/<int:id>', views.admin_athletes_details, name='admin_athletes_details'),
    path('deleteathletes/<int:id>', views.delete_athletes, name='delete_athletes'),


    path('ahitcounter/', views.admin_hit_counter, name='admin_hit_counter'),
]