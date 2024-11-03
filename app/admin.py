from django.contrib import admin
from . import models

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(models.TaskCompletionRecord)
class TaskCompletionRecordAdmin(admin.ModelAdmin):
    pass

@admin.register(models.HouseMember)
class HouseMemberAdmin(admin.ModelAdmin):
    pass

# Register your models here.
