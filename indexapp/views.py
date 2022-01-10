# from django.http import HttpResponse
import datetime

from django.shortcuts import render


# def now(request):
#
#     now = datetime.datetime.now()
#
#     msg = f'Today is {now} \n ! riabow.com is under construction !'
#
#     return HttpResponse(msg, content_type='text/plain')

def index_view(request):
    now = datetime.datetime.now()
    return render(request,
                  'indexapp/indexapp.html',
                  context={'current_date': now})
