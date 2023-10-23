from django.contrib import admin
from .models import Partner,Gallery,Patron,Team,Event
# Models registration.

class PartnerAdmin(admin.ModelAdmin):
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
class EventAdmin(admin.ModelAdmin):
   ordering = ["id"]
   list_display = ["etitle", "etopic", "estatus", "eurl", "edate", "ebanner", "eslide"]

class TeamAdmin(admin.ModelAdmin):
  ordering = ["id"]
  list_display = ["tname", "tpost", "taccademicyear", "tgithub", "tlinkedin", "ttwitter", "tphoto"]
  
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Patron, PatronAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Team, TeamAdmin)