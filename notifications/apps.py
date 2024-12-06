from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'
    # Automatically imports signal when the app is ready

    def ready(self):
        import notifications.signals
