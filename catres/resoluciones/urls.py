from django.urls import path
from . import views

urlpatterns = [
    # path('resoluciones/', views.resoluciones, name='resoluciones')
    path('resoluciones/',views.ResolucionesListView.as_view(), name='resoluciones'
    )
    
]
