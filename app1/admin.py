from django.contrib import admin

from app1.models import VW_Car, Part

class VWCarAdmin(admin.ModelAdmin):
    pass

class PartAdmin(admin.ModelAdmin):
    pass

admin.site.register(VW_Car, VWCarAdmin)
admin.site.register(Part, PartAdmin)


