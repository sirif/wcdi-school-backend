from django.apps import AppConfig


class ObjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'objects'

    def ready(self) -> None:
        import objects.signals
