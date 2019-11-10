from django.contrib import admin
from django.urls import path, include
from tindartapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.Homepage.as_view(), name='homepage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user/', views.User, name='user'),
    path('artist/', views.Artist, name='artist'),
    path('art/', views.Art, name='art'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
