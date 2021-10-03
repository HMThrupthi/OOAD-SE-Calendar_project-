import datetime
from datetime import timedelta, date
import time
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
import ssl
from .models import *
from .utils import Calendar
from .forms import EventForm,DelEventForm,EmailForm
import csv
from json import dumps
import smtplib

def index(request):
    return HttpResponse('hello')



class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.date.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def login(request,event_id = None):
    file = "login_det"
    csv_fp = open(f'{file}.csv', 'r')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    print(out)
    headers = dumps(headers)
    row = dumps(out)
    return render(request, 'cal/login.html',{'row': row,headers:'headers'})

    return render(request,'cal/login.html')

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    forming = str(form)
    file1 = open("eventlogs.txt", "a")
    #file2 = open("login_det.csv","r")
    #for i in file2:
    #    print(i)

    file1.write("Title  ")
    file1.write("Start Date       ")
    file1.write("End Date         ")
    file1.write("\n")
    for i in forming.split(" "):
        if "value" in i:
            file1.write(i[7:])
            file1.write(" ")
    file1.write("\n")
    return render(request, 'cal/event.html', {'form': form})
def emails(request):

    '''
    five_minutes = datetime.timedelta(minutes=5)
    final_datetime = initial_datetime - five_minutes
    print("reminder time = ",final_datetime)
    current_time = datetime.datetime.now()
    print("current time = ",current_time)
    print(final_datetime.timestamp() - current_time.timestamp())
    #time.sleep(final_datetime.timestamp() - current_time.timestamp())


    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "bhargu2000@gmail.com" 
    password = "qwerty@123"
    message = """
    Subject: Calendar App
            
    Hello
    Your event is starting in 5 minutes."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        #x = time.sleep(send_time.timestamp() - time.time())
        for i in range(len(email_list)):
            server.sendmail(sender_email, email_list[i], message)
    '''
    return render(request, 'cal/emails.html')

    
    #email_list = ["thrupthijyo22@gmail.com","nishasuresh2001@gmail.com", "bhargu2000@gmail.com"]
    #initial_datetime = datetime.datetime(2021, 4, 7, 10, 25, 0)
    #email_notify(email_list, initial_datetime)
    

def delevent(request, event_id=None):
    instance = DelEvent()
    if event_id:
        instance = get_object_or_404(DelEvent, pk=event_id)
    else:
        instance = DelEvent()

    form = DelEventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    
    return render(request, 'cal/event.html', {'form': form})


    


