from django.contrib import admin
from django.urls import path, include
from tindartapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.Homepage.as_view(), name='homepage'),
	path('main/<slug:pk>/', views.Artworks.as_view(), name='mainpage'),
	path('redirect/', views.redirect, name='redirect'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('art/', views.ArtView, name='art'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
