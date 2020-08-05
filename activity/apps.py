from django.apps import AppConfig, apps


class ActivityConfig(AppConfig):
    name = 'activity'

    def ready(self):
        from actstream import registry
        import activity.signals
        registry.register(apps.get_model('auth.user')) #registers the User (assuming you're using auth.User)
        registry.register(apps.get_model('publications.publication'))
