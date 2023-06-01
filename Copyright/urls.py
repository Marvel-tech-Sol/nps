from django.urls import path
from . import views
urlpatterns=[
    path("table/",views.Copyrighttableview),
    path("application/",views.Copyrightapplicationview,name = 'copyrightapplication'),
    path("status/<str:uid>",views.Copyrightstatusview),
    path("CopyrightStatusup",views.CopyrightStatusup,name='CopyrightStatusup'),
    path('deletecopyright/<str:uid>',views.delepteAppCopyright,name='deletecopyright')
]