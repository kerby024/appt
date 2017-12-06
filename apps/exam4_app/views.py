# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..logreg_app.models import User
from .models import Appt
import datetime
def display(request):
    today_appts = Appt.objects.filter(user_id = request.session['id'], date=datetime.date.today())
    all_appts = Appt.objects.filter(user_id = request.session['id'])

    ta = set(today_appts)
    aa = set(all_appts)

    aa -= ta
    
    now = Appt(date=datetime.date.today())
    no = Appt(date = datetime.date.today())
    context = {
         'now' :now,
        'users' :User.objects.all(),
        'appt': Appt.objects.filter(user_id = request.session['id'], date=datetime.date.today()),
        'future': aa
        # 'no_fave' : ato
    }
    return render(request, 'exam4_app/display.html', context)

def newappt(request):
    errors = Appt.objects.appt_validation(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/exam4/display')
    else:
        user = User.objects.get(id = request.session['id'])
        new = Appt.objects.create(
            date = request.POST['date'],
            time = request.POST['time'],
            tasks = request.POST['task'],
            status = 'Pending',
            user = user
        )
    return redirect('/exam4/display')

def update(request, apptid):
    user = User.objects.get(id = request.session['id'])
    appointment = Appt.objects.get(id=apptid)
    context = {
        'update' :Appt.objects.filter(id = apptid)
    }
    return render(request, 'exam4_app/update.html', context)

def process(request, apptid):
    errors = Appt.objects.appt_validation(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/exam4/appt/{}'.format(apptid))

    else:
        user = User.objects.get(id = request.session['id'])
        updateappointment = Appt.objects.get(id=apptid)
        updateappointment.user = user
        updateappointment.date = request.POST['date']
        updateappointment.time = request.POST['time']
        updateappointment.tasks = request.POST['task']
        updateappointment.status = request.POST['status']
        updateappointment.save()
    
    return redirect('/exam4/display')

def delete(request, apptid):
    appointment = Appt.objects.get(id=apptid).delete()
    return redirect('/exam4/display')

def clear(request):
    request.session.flush()
    return redirect('/')
# Create your views here.
