from django.contrib import admin
from .models import Partner,Gallery,Patron,Team,Event,Technologies,StudentRegistration
from django.http import HttpResponse
from django.urls import path
from import_export import resources



# Models registration.
class PartnerAdmin(admin.ModelAdmin):
  actions_on_top = False
  actions_on_bottom = False
  ordering = ["id"]
  list_display = ("edit", "pname", "pwebsite", "plogo")
  def edit(self,obj):
        return f"Edit"
  edit.short_description = 'Record'

class GalleryAdmin(admin.ModelAdmin):
  ordering = ["id"]
  list_display = ["edit", "gimage", "gdescription", "gyear"]
  def edit(self,obj):
        return f"Edit"
  edit.short_description = 'Record'

class PatronAdmin(admin.ModelAdmin):
  ordering = ["id"]
  list_display = ["edit", "Pavater", "Pname", "Padvice", "Pdesignation"]
  def edit(self,obj):
        return f"Edit"
  edit.short_description = 'Record'

class EventAdmin(admin.ModelAdmin):
   ordering = ["id"]
   list_display = ["edit", "etitle", "etopic", "estatus", "eurl", "edate", "ebanner", "eslide"]
   def edit(self,obj):
        return f"Edit"
   edit.short_description = 'Record'

class TeamAdmin(admin.ModelAdmin):
  ordering = ["id"]
  list_display = ["edit", "tname", "tpost", "taccademicyear", "tgithub", "tlinkedin", "ttwitter", "tphoto"]
  def edit(self,obj):
        return f"Edit"
  edit.short_description = 'Record'

class TechnologiesAdmin(admin.ModelAdmin):
   ordering = ["id"]
   list_display = ["edit", "tTitle", "tDescription", "tPhoto", "tUrl"]
   def edit(self,obj):
        return f"Edit"
   edit.short_description = 'Record'



class StudentResource(resources.ModelResource):
    class Meta:
        model = StudentRegistration
        fields = (
            'kyucsaId', 'firstName', 'lastName', 'programme', 'gender', 'academicStatus',
            'studentNumber', 'enrollmentYear', 'email', 'mobileNumber', 'registeredAt'
        )
        export_order = fields


class StudentAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["edit", "kyucsaId", "firstName", "lastName", "programme", "gender", "academicStatus",
                    "studentNumber", "enrollmentYear", "email", "mobileNumber", "registeredAt"]
    readonly_fields = ["kyucsaId"]  # to avoid editing the ID
    actions = ["export_as_excel"]

    def edit(self, obj):
        return f"Edit"
    edit.short_description = 'Record'

    def export_as_excel(self, request, *args, **kwargs):
        student_resource = StudentResource()
        dataset = student_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=kyucsa_students.xlsx'
        return response

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('export_as_excel/', self.export_as_excel, name='export_as_excel'),
        ]
        return my_urls + urls





admin.site.register(StudentRegistration,StudentAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Patron, PatronAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Technologies, TechnologiesAdmin)