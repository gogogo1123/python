from address import views
from django.urls import path


urlpatterns = [

    path('', views.home), # http:localhost/address
    path('write', views.write),
    path('insert', views.insert),
    path('detail', views.detail),
    path('update', views.update),
    path('delete', views.delete),
]



