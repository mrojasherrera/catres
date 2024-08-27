from django.http import HttpResponse
from django.template import loader
from .models import Resoluciones

# Create your views here.

def resoluciones(request):
    misresoluciones = Resoluciones.objects.all().values()
    template = loader.get_template('resoluciones.html')
    context = {
        'misresoluciones': misresoluciones,
    }
    return HttpResponse(template.render(context, request))