#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
#import ptvsd

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    # comment in the following 2 lines to debug tests in container, then run
    # 'docker-compose run app python manage.py test' and use launch config "Python: Remote Attach")
#    ptvsd.enable_attach(address=('0.0.0.0', 5678))
#    ptvsd.wait_for_attach()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
