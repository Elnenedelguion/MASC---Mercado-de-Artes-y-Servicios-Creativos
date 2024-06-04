from django.apps import AppConfig


class ModelosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aplicaciones.modelos'
    verbose_name = 'Modelos de la Aplicación'

    def ready(self):
        import Aplicaciones.modelos.signals