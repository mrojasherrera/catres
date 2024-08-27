# from django.http import HttpResponse
# from django.template import loader
# from .models import Resoluciones
# 
# from django.shortcuts import render
# from .forms import ResolucionesSearchForm

from django.views.generic import ListView
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .models import Resoluciones

# Create your views here.
# -----------------------

# solución basada en FBV (vista basada en función)
# def resoluciones(request):
#     misresoluciones = Resoluciones.objects.all().values()
#     template = loader.get_template('resoluciones.html')
#     context = {
#         'misresoluciones': misresoluciones,
#     }
#     return HttpResponse(template.render(context, request))

class ResolucionesListView(ListView):
    model = Resoluciones
    template_name = 'resoluciones_list.html'
    context_object_name = 'misresoluciones'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = super().get_queryset()
            query = self.request.GET.get('q')

            if query:
                search_query = SearchQuery(query)
                queryset = queryset.filter(tsbuscar = search_query)

        return queryset
