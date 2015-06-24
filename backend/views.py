from django.shortcuts import redirect
from .models import Party, Song
# Create your views here.

def add_party(request):
	name = request.POST['name']
	party = Party.objects.create(name=name)
	return redirect('index')

def add_song(request):
	name = request.POST['name']
	party_id = request.POST['party']
	p = Party.objects.get(id=party_id)
	Song.objects.create(party=p, name=name, votes=1)
	return redirect(p)

def add_vote(request, song_id):
	s = Song.objects.get(id=song_id)
	s.votes += 1
	s.save()
	return redirect(s.party)