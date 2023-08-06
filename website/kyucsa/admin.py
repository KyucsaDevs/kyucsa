from django.contrib import admin
from .models import Partners,Gallery,Team,Events
# Models registration.

class PartnersAdmin(admin.ModelAdmin):
  ordering = ["id"]
  list_display = ("pname", "pwebsite", "plogo")
#class GalleryAdmin(admin.ModelAdmin):
#  ordering = ('year')
#  list_display = ("gimage", "gdescription", "year")
#class TeamAdmin(admin.ModelAdmin):
#  list_display = ("tfullname", "tposition", "taccademicyear", "tgithub", "tlinkedlin", "ttwitter", "tprofilepicture")
#class EventAdmin(admin.ModelAdmin):
#  list_display = ("etitle", "etopic", "estatus", "eurl", "edate", "ebanner")

  
admin.site.register(Partners, PartnersAdmin)
#admin.site.register(Gallery, GalleryAdmin)
#admin.site.register(Team, TeamAdmin)
#admin.site.register(Events, EventAdmin)
