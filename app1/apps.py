from django.apps import AppConfig


class App1Config(AppConfig):
    '''
    main app is placed here
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'
