from django.contrib import admin
from django.urls import path
from Campeones import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Home),
    path("campeones/", views.Campeones_list, name="campeones"),
    path("campeones/<int:campeon_id>/", views.campeon_detail, name="campeon_detail")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)