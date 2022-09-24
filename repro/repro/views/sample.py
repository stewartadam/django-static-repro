from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def foo(request):
    from django.template import engines
    django_engine = engines['django']
    from django.conf import settings
    html = ""
    html += "FORCE_SCRIPT_NAME: %s\n" % settings.FORCE_SCRIPT_NAME
    html += "STATIC_URL: %s\n" % settings.STATIC_URL # Note: in settings.py it is 'static/' but the output here will include FORCE_SCRIPT_NAME
    html += "call static for test_file: %s\n" % django_engine.from_string("{% load static %}{% static 'test_file' %}").render()

    return HttpResponse(html)