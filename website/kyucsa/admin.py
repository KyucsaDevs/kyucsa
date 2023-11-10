from django.contrib import admin
from .models import Partner,Gallery,Patron,Team,Event,Technologies,StudentRegistration
# Models registration.

class PartnerAdmin(admin.ModelAdmin):
  actions_on_top = False
  actions_on_bottom = False
  ordering = ["id"]
  list_display = ("edit", "pname", "pwebsite", "plogo")
  def edit(self,obj):
        return f"Edit Information"
  edit.short_description = 'Edit Partner Information'
  edit.allow_tags = True

class GalleryAdmin(admin.ModelAdmin):
  ordering = ["id"]
  list_display = ["edit", "gimage", "gdescription", "gyear"]
  def edit(self,obj):
        return f"Edit Information"
  edit.short_description = 'Edit Gallery Information'
  edit.allow_tags = True

class PatronAdmin(admin.ModelAdmin):
  ordering = ["id"]
  list_display = ["edit", "Pavater", "Pname", "Padvice", "Pdesignation"]
  def edit(self,obj):
        return f"Edit Information"
  edit.short_description = 'Edit Partron Information'
  edit.allow_tags = True

class EventAdmin(admin.ModelAdmin):
   ordering = ["id"]
   list_display = ["etitle", "etopic", "estatus", "eurl", "edate", "ebanner", "eslide"]
   def edit(self,obj):
        return f"Edit Information"
   edit.short_description = 'Edit Event Details'
   edit.allow_tags = True

class TeamAdmin(admin.ModelAdmin):
  ordering = ["id"]
  list_display = ["edit", "tname", "tpost", "taccademicyear", "tgithub", "tlinkedin", "ttwitter", "tphoto"]
  def edit(self,obj):
        return f"Edit Information"
  edit.short_description = 'Edit Team Information'
  edit.allow_tags = True

class TechnologiesAdmin(admin.ModelAdmin):
   ordering = ["id"]
   list_display = ["edit", "tTitle", "tDescription", "tPhoto", "tUrl"]
   def edit(self,obj):
        return f"Edit Information"
   edit.short_description = 'Edit Technology'
   edit.allow_tags = True

class StudentRegistrationAdmin(admin.ModelAdmin):
   ordering = ["id"]
   list_display = ["edit", "kyucsaId","firstName", "lastName", "programme", "gender","academicStatus",
                   "studentNumber", "enrollmentYear","email", "mobileNumber", "registeredAt"]
   def edit(self,obj):
        return f"Information"
   edit.short_description = 'View Details'
   edit.allow_tags = True


admin.site.register(StudentRegistration,StudentRegistrationAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Patron, PatronAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Technologies, TechnologiesAdmin)