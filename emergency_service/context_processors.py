import datetime


def now(request):
    now = datetime.datetime.now()
    context = {
        'now': now
    }
    return context
