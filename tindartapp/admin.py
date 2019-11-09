from django.contrib import admin
from tindartapp.models import User, Artist, Art

class UserAdmin(admin.ModelAdmin):
	list_display = (
        'username',
    )
admin.site.register(User, UserAdmin)

class ArtistAdmin(admin.ModelAdmin):
	list_display = (
        'username',
    )
admin.site.register(Artist, ArtistAdmin)

class ArtAdmin(admin.ModelAdmin):
	list_display = (
        'artist',
    )
admin.site.register(Art, ArtAdmin)