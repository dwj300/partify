from django.shortcuts import render
from backend.models import Party
# Create your views here.

def index(request):
	parties = Party.objects.all()
	context = {'parties': parties}
	return render(request, 'index.html', context)

def party(request, party_id):
	p = Party.objects.get(id=party_id)
	context = {'party': p}
	return render(request, 'party.html', context)