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
    path('Ideastatusdata',views.Ideastatusdata,name='Ideastatusdata'),
    path('ferstatusview/<str:uid>',views.FerstatusView,name='ferstatusview/'),
    path('ideastatusview/<str:uid>',views.ideadevelopmentstatusview,name='ideastatusview/'),
    path('HearingStatus',views.Hearingstatusdata,name='HearingStatus'),
    path('GrantStatus',views.GrantsStatusdata,name='GrantStatus'),
    path('PaymentStatus',views.PaymentStatus,name='PaymentStatus'),

    #approve
    path('approvenovelty/<str:uid>',views.approvenovelty,name = 'approvenovelty/'),
    path('approvedrafting/<str:uid>',views.approvedraft,name = 'approvedrafting/'),
    path('approvefer/<str:uid>',views.approvefer,name = 'approvefer/'),
    path('approvedrawing/<str:uid>',views.approvedrawing,name = 'approvedrawing/'),


    #reassign
    path('reassignnovelty/<str:uid>',views.reassignnovelty,name='reassignnovelty/'),
    path('reassigdrafting/<str:uid>',views.reassigndraft,name='reassigdrafting/'),
    path('reassigfer/<str:uid>',views.reassignfer,name='reassigfer/'),
    path('reassigdrawing/<str:uid>',views.reassigndrawing,name='reassigdrawing/'),
]