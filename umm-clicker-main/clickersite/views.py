from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.timezone import datetime
from .models import Times, Presentors
import time
import re

# Create your views here.

def home(request):
    if request.method == "POST":
        speakers = Presentors
        name = request.POST['name']

        if not speakers.objects.filter(name=name).exists():
            speaker_instance = speakers.objects.create(name=name)

        return redirect(time, speaker=name)

    return render(
        request,
        'clickerpage/name.html'
    )

def time(request, speaker):
    pres_id = int(Presentors.objects.filter(name=speaker).first().pk)
    times = Times.objects.filter(pres_id=pres_id).all()
    
    if request.method == "POST":
        time = datetime.now()
        if Times.objects.filter(pres_id=pres_id).exists():
            time = Times.objects.filter(pres_id=pres_id).last().time
        datetime_now = datetime.now()
        time_instance = Times.objects.create(pres_id=pres_id, time=datetime_now)

    else:
        print(request.build_absolute_uri())
        datetime_now = datetime.now()
    timediff = 0

    return render(
        request,
        'clickerpage/clicker_page.html',
        {
            'speaker': speaker,
            'times': times,
            'timedifference': timediff
        }
    )