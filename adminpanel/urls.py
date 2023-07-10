from django.urls import path

import adminpanel.views
from . import views

urlpatterns = [
    path("", views.adminpanel, name='adminpanel/'),
    path('editapplication/<str:uid>', views.Editapplication, name='editapplication'),
    path('editapplicationcopyright/<str:uid>', views.EditapplicationCopyright, name='editapplicationcopyright'),
    path('ndastatus', views.ndsatatus, name='ndastatus'),
    path('closeapplication', views.closeapplication, name='closeapplication'),
    path('openapplication', views.openapplication, name='openapplication'),
    path('FilingStatus', views.filingstatus, name='FilingStatus'),
    path('track', views.track, name='track'),
    path('assignto', views.assignto, name='assignto'),
    path('reports', views.generateworkbook, name='reports'),
    path('delete/<str:uid>', views.deleteApp, name='delete'),
]
