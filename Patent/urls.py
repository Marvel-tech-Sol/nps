from django.urls import path
from . import views
urlpatterns=[
    path("fullpatentapplication",views.FullPatentapplicationview,name ='fullpatentapplication'),
    path("patentapplication",views.Patentapplicationview,name = 'patentapplication'),
    path("documentationstatus/<str:uid>",views.Documentationstatusview,name = 'documentationstatus/'),
    path("documentationtable",views.Documentationtableview),
    path("draftingstatus/<str:uid>",views.Draftingstatusview,name = 'draftingstatus/'),
    path("draftingtable",views.Draftingtableview),
    path("drawingstatus/<str:uid>",views.Drawingstatusview,name = 'drawingstatus/'),
    path("drawingtable",views.Drawingtableview),
    path("patentabilitysearchstatus/<str:uid>",views.Patentabilitysearchstatusview,name= 'patentabilitysearchstatus/'),
    path("patentabilitysearchtable",views.Patentabilitysearchtableview),
    path('NoveltyStatus',views.Patentabilitysearchstatusdata,name = "NoveltyStatus"),
    path('DraftingStatus',views.Draftingstatusdata,name='DraftingStatus'),
    path('DrawingStatus',views.Drawingstatusdata,name='DrawingStatus'),
    path('DocumentationStatus',views.Documentationstatusdata,name='DocumentationStatus'),
    path('FilingStatus',views.FilingStatusdata,name=" FilingStatus"),
    path('ExaminationStatus',views.ExaminationSatusdata,name='ExaminationStatus'),
    path('FerStatus',views.FerStatusdata,name='FerStatus'),
    path('HearingStatus',views.Hearingstatusdata,name='HearingStatus'),
    path('GrantStatus',views.GrantsStatusdata,name='GrantStatus'),
    path('PaymentStatus',views.PaymentStatus,name='PaymentStatus'),

]