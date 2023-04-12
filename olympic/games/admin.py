from django.contrib import admin

from games.models import BroadcastVideo, GamesCategory, Hitcount, Schedule, Scoreboards, HighlightsVideo,Athletes


admin.site.register(GamesCategory)
admin.site.register(Scoreboards)
admin.site.register(BroadcastVideo)
admin.site.register(Schedule)
admin.site.register(HighlightsVideo)
admin.site.register(Hitcount)
admin.site.register(Athletes)