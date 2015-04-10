from django.shortcuts import render
from django.http import HttpResponse

from summerbeer import models

# Create your views here.
def index(request):
    beers = models.Beer.objects.order_by("rank").all()
    context = {
        "beers": beers,
    }
    return render(request, 'summerbeer/index.html', context)
