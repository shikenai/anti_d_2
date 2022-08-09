from django.shortcuts import render
from app_anti_d.models import DisasterName
from .forms import FormDisasterName


# Create your views here.

def index(request):
    return render(request, 'index.html')


def disasters(request):
    all_disasters = DisasterName.objects.order_by('-start_date')
    if request.method == 'POST':
        form = FormDisasterName(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
    return render(request, 'all_disasters.html', {
        "disasters": all_disasters,
        "form": FormDisasterName
    })


def disaster(request, disaster_id):
    _disaster = DisasterName.objects.get(pk=disaster_id)
    return render(request, 'disaster.html', {
        "d": _disaster
    })

