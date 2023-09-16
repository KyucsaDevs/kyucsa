from django.apps import AppConfig


class KyucsaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kyucsa'

    def ready(self):
        import kyucsa.signals