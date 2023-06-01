from django.contrib import admin
from .models import Patentapplication, NDAStatus, PaymentStatus, NoveltyStatus, DocumentationStatus, DrawingStatus, \
    DraftingStatus, FerStatus, ExaminationSatus, FilingStatus, HearingStatus, GrantsStatus,Assignedto

# Register your models here.

admin.site.register(Patentapplication)
admin.site.register(NDAStatus)
admin.site.register(PaymentStatus)
admin.site.register(NoveltyStatus)
admin.site.register(DrawingStatus)
admin.site.register(DocumentationStatus)
admin.site.register(GrantsStatus)
admin.site.register(HearingStatus)
admin.site.register(ExaminationSatus)
admin.site.register(DraftingStatus)
admin.site.register(FerStatus)
admin.site.register(FilingStatus)
admin.site.register(Assignedto)
