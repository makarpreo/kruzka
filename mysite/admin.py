from django.contrib import admin
from .models import GeeksModel


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(GeeksModel, MovieAdmin)
# Register your models here.
