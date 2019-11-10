from django.contrib import admin
from tindartapp.models import Art

class ArtAdmin(admin.ModelAdmin):
	list_display = (
        'user',
    )
admin.site.register(Art, ArtAdmin)