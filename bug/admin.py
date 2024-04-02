from django.contrib import admin
from .models import *

class BugAdmin(admin.ModelAdmin):
    list_display = ('id','bug_title','status',)
    list_filter = ('status','priority','category',)
    search_fields = ('bug_detail','id')
    ordering = ('id',)

    def get_queryset(self, request):
        qs = super(BugAdmin, self).get_queryset(request)
        qs = qs.exclude(status="FIXED")
        qs = qs.exclude(status="HOLD")
        return qs


# Register your models here.
admin.site.register(Bug, BugAdmin)
