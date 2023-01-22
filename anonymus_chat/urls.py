from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from chat.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor", include("ckeditor_uploader.urls")),
    path("", index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
