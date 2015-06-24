from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Party(models.Model):
    name = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('party_details', args=[str(self.id)])

    @property
    def get_top_songs(self):
        return Song.objects.filter(party=self).order_by('-votes')[:10]





class Song(models.Model):
    party = models.ForeignKey(Party)
    name = models.CharField(max_length=150)
    votes = models.IntegerField()
