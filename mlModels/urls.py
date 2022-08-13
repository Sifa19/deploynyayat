from django.urls import path
from . import views

urlpatterns = [
    path('query',views.search),
    path('',views.predictor,name='predictor'),
    
]
