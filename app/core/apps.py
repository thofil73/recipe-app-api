from django.apps import AppConfig

# import ptvsd


class CoreConfig(AppConfig):
    name = 'core'

    # enable debugger to attach to running application
    # (use launch config "Python: Remote Attach")
    # ptvsd.enable_attach(address=('0.0.0.0', 5678))
    # ptvsd.wait_for_attach()
