from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Projects, Messages
from .forms import Mes
from django.views.decorators.http import require_POST

def start(request):
	return redirect('main_page')

def main_page(request):
	p=Projects.objects.all()
	contex={'p':p}
	return render(request, 'main/index.html', contex)

def contact(request):
	return render(request, 'contact/cont.html')

def write_me(request):
	m=Mes()
	contex={'m':m}
	return render(request, 'write_me/write.html', contex)

def for_me(request):
	my_mes=Messages.objects.all()
	contex={'my_mes':my_mes}
	return render(request, 'my.html', contex)

@require_POST
def add_a_message(request):
	form_for_m=Mes(request.POST)
	if form_for_m.is_valid():
		Messages(when=request.POST,title=request.POST['title_f'],message=request.POST['message_f'],name_writer=request.POST['name_f']).save()
	return redirect('write_me')

# def error(request, for_error):
# 	contex={'for_error': for_error}
# 	return render(request, '404.html', contex)