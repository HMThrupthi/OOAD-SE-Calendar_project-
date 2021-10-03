from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
 

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
       
        return f'<a href="{url}"> {self.title} </a>'
class Email(models.Model):
    name = models.CharField(max_length=200)
    event_id = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    email1 = models.TextField()
    email2 = models.TextField()
    email3 = models.TextField()
 

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
       
        return f'<a href="{url}"> {self.title} </a>'


class DelEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_del', args=(self.id,))
       
        return f'<a href="{url}"> {self.title} </a>'
    

