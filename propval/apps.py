from django.apps import AppConfig


class PropvalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'propval'

    def ready(self):
        import propval.signals  # noqa: F401
