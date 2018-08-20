from django.shortcuts import render
from .models import Event

def blog(request):
	e=Event.objects.all()
	contex={'e':e}
	return render(request, 'blog/blog.html', contex)

def every_event(request, id_event):
	event=Event.objects.get(id=id_event)
	contex={'event': event}
	return render(request, 'event/evryevent.html', contex)
