from django.contrib import admin
from app_anti_d import models
# Register your models here.
admin.site.register(models.DisasterName)
admin.site.register(models.LocalGovernments)
admin.site.register(models.HearingReportsFromLocalGovernment)