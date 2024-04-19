from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

#admin ui edits
admin.site.site_header="Administrator"
admin.site.site_title="Dashboard"
urlpatterns = [
    path('', include('App.urls')),
    path('administrator/', admin.site.urls),
]
handler404 = 'App.views.custom_404'
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)