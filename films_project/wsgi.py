import os
import threading
import subprocess
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "films_project.settings")

application = get_wsgi_application()



