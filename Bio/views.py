from django.shortcuts import render
from Bio.models import Bio

# Create your views here.
def BioIndex(request):
    bio = Bio.objects.get()
    context = {
        'bio': bio
    }
    return render(request, 'bio_index.html', context)