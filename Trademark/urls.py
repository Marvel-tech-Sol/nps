from django.urls import path
from . import views

urlpatterns = [
    path("application/", views.Trademarkapplicationview, name='trademarkapplication'),
    path("status//<str:uid>'", views.Trademarkstatusview),
    path("table/", views.Trademarktableview),

]
