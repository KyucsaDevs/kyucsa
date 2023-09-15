from django.contrib import admin
from .models import Partners,Gallery,Patron,Team,Events
# Models registration.

class PartnersAdmin(admin.ModelAdmin):
  ordering = ["id"]
  list_display = ("pname", "pwebsite", "plogo")
class GalleryAdmin(admin.ModelAdmin):
  ordering = ["id"]
  list_display = ["gimage", "gdescription", "gyear"]
class PatronAdmin(admin.ModelAdmin):
  ordering = ["id"]
  list_display = ["Avater", "Pavater", "Pname", "Pdesignation"]
  def Avater(self, obj):
        return f"Edit Details"
  Avater.short_description = 'Editing'
  Avater.allow_tags = True

#class TeamAdmin(admin.ModelAdmin):
#  list_display = ["tfullname", "tposition", "taccademicyear", "tgithub", "tlinkedlin", "ttwitter", "tprofilepicture"]
#class EventAdmin(admin.ModelAdmin):
#  list_display = ["etitle", "etopic", "estatus", "eurl", "edate", "ebanner"]

  
admin.site.register(Partners, PartnersAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Patron, PatronAdmin)
#admin.site.register(Team, TeamAdmin)
#admin.site.register(Events, EventAdmin)
