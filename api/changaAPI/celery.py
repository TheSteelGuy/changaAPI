from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'changaAPI.settings')
app = Celery('tasks', backend='redis://localhost:6379', broker='redis://localhost:6379')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'callback_not_rec': {
        'task': 'changaAPI.apps.callbacks.tasks.callback_not_received',
        'schedule': crontab(),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

