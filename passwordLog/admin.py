from django.contrib import admin
from passwordLog.models import CheckAudioName

class AuthorisationAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(CheckAudioName,AuthorisationAdmin)
